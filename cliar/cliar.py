from argparse import ArgumentParser, RawTextHelpFormatter
from inspect import signature, getmembers, ismethod
from collections import OrderedDict
from typing import List, Iterable, Callable, Set, Type

from .utils import ignore


# pylint: disable=too-few-public-methods,protected-access, too-many-instance-attributes


class _Arg:
    '''CLI command argument.

    Its attributes correspond to the homonymous params of the ``add_argument`` function.
    '''

    def __init__(self):
        self.type = None
        self.default = None
        self.action = None
        self.nargs = None
        self.metavar = None
        self.help = None
        self.short_name = None


class _Command:
    '''CLI command corresponding to a handler.

    Command args correspond to its handler args.
    '''

    def __init__(self, handler: Callable):
        self.handler = handler

        if hasattr(handler, '_arg_map'):
            self.arg_map = handler._arg_map
        else:
            self.arg_map = {}

        if hasattr(handler, '_sharg_map'):
            self.sharg_map = handler._sharg_map
        else:
            self.sharg_map = {}

        if hasattr(handler, '_metavar_map'):
            self.metavar_map = handler._metavar_map
        else:
            self.metavar_map = {}

        if hasattr(handler, '_command_name'):
            self.name = handler._command_name
        else:
            self.name = handler.__name__.replace('_', '-')

        if hasattr(handler, '_command_aliases'):
            self.aliases = handler._command_aliases
        else:
            self.aliases = []

        if hasattr(handler, '_help_map'):
            self.help_map = handler._help_map
        else:
            self.help_map = {}

        self.args = self._get_args()

    @staticmethod
    def _get_origins(typ) -> Set[Type]:
        '''To properly parse arg types like ``typing.List[int]``, we need a way to determine that
        the type is based on ``list`` or ``tuple``. In Python 3.6, we'd use subclass check,
        but it doesn't work anymore in Python 3.7. In Python 3.7, the right way to do such a check
        is by looking at ``__origin__``.

        This method checks the type's ``__origin__`` to detect its origin in Python 3.7
        and ``__orig_bases__`` for Python 3.6.
        '''

        origin = getattr(typ, '__origin__', None)
        orig_bases = getattr(typ, '__orig_bases__', ())

        return set((origin, *orig_bases))

    def _get_args(self) -> OrderedDict:
        '''Get command arguments from the parsed signature of its handler.'''

        args = OrderedDict()

        handler_signature = signature(self.handler)

        for param_name, param_data in handler_signature.parameters.items():
            arg = _Arg()

            arg.help = self.help_map.get(param_name, '')

            if param_data.annotation is not param_data.empty:
                arg.type = param_data.annotation

            if param_data.default is not param_data.empty:
                arg.default = param_data.default

                if not arg.type:
                    arg.type = type(arg.default)

            if arg.type == bool:
                arg.action = 'store_true'

            elif self._get_origins(arg.type) & {list, tuple}:
                if arg.default:
                    arg.nargs = '*'
                else:
                    arg.nargs = '+'

                if arg.type.__args__:
                    arg.type = arg.type.__args__[0]

            if not arg.action and param_name in self.metavar_map:
                arg.metavar = self.metavar_map[param_name]

            if param_name not in self.arg_map:
                self.arg_map[param_name] = param_name.replace('_', '-')

            arg.short_name = self.sharg_map.get(param_name, self.arg_map[param_name][0])

            args[self.arg_map[param_name]] = arg

        return args


class Cliar:
    '''Base CLI class.

    Subclass from it to create your own CLIs.

    A few rules apply:

    -   Regular methods are converted to commands. Such methods are called *handlers*.
    -   Command args are generated from the corresponding method args.
    -   Methods that start with an underscore are ignored.
    -   ``self._root`` corresponds to the class itself. Use it to define global args.
    '''

    def __init__(self):
        self._parser = ArgumentParser(
            description=self.__doc__,
            formatter_class=RawTextHelpFormatter
        )

        self._register_root_args()

        self._commands = {}

        handlers = self._get_handlers()

        if handlers:
            self._command_parsers = self._parser.add_subparsers(
                dest='command',
                title='commands',
                help='Available commands:'
            )

            self._register_commands(handlers)

    def _register_root_args(self):
        '''Register root args, i.e. params of ``self._root``, in the global argparser.'''

        self.root_command = _Command(self._root)

        for arg_name, arg_data in self.root_command.args.items():
            self._register_arg(self._parser, arg_name, arg_data)

    @staticmethod
    def _register_arg(command_parser: ArgumentParser, arg_name: str, arg_data: _Arg):
        '''Register an arg in the specified argparser.

        :param command_parser: global argparser or a subparser corresponding to a CLI command
        :param str arg_name: handler param name without prefixing dashes
        :param arg_data: arg type, default value, and action
        '''

        if arg_data.default is None:
            arg_prefixed_names = [arg_name]

        elif arg_data.short_name:
            arg_prefixed_names = ['-'+arg_data.short_name, '--'+arg_name]

        else:
            arg_prefixed_names = ['--'+arg_name]

        if arg_data.action:
            command_parser.add_argument(
                *arg_prefixed_names,
                default=arg_data.default,
                action=arg_data.action,
                help=arg_data.help
            )

        elif arg_data.nargs:
            command_parser.add_argument(
                *arg_prefixed_names,
                type=arg_data.type,
                default=arg_data.default,
                nargs=arg_data.nargs,
                metavar=arg_data.metavar,
                help=arg_data.help
            )

        else:
            command_parser.add_argument(
                *arg_prefixed_names,
                type=arg_data.type,
                default=arg_data.default,
                metavar=arg_data.metavar,
                help=arg_data.help
            )

    def _get_handlers(self) -> List[Callable]:
        '''Get all handlers except ``self._root``.'''

        return (
            method
            for method_name, method in getmembers(self, predicate=ismethod)
            if not method_name.startswith('_') and not hasattr(method, '_ignore')
        )

    def _register_commands(self, handlers: Iterable[Callable]):
        '''Create parsers for commands from handlers (except for ``self._root``).'''

        for handler in handlers:
            command = _Command(handler)

            command_parser = self._command_parsers.add_parser(
                command.name,
                help=handler.__doc__.splitlines()[0] if handler.__doc__ else '',
                description=handler.__doc__,
                formatter_class=RawTextHelpFormatter,
                aliases=command.aliases
            )

            for arg_name, arg_data in command.args.items():
                self._register_arg(command_parser, arg_name, arg_data)

            self._commands[command.name] = command

            for alias in command.aliases:
                self._commands[alias] = command

    @ignore
    def parse(self):
        '''Parse commandline input, i.e. launch the CLI.'''

        args = self._parser.parse_args()

        if self._commands:
            command = self._commands.get(args.command)

            if command:
                command_args = {arg: vars(args)[arg.replace('-', '_')] for arg in command.args}

                inverse_arg_map = {arg: param for param, arg in command.arg_map.items()}

                command.handler(
                    **{inverse_arg_map[arg]: value for arg, value in command_args.items()}
                )

            else:
                root_args = {arg: vars(args)[arg] for arg in self.root_command.args}

                inverse_root_arg_map = {
                    arg: param for param, arg in self.root_command.arg_map.items()
                }

                if self.root_command.handler(
                        **{inverse_root_arg_map[arg]: value for arg, value in root_args.items()}
                    ) == NotImplemented:
                    self._parser.print_help()


    def _root(self):
        '''The root command, which corresponds to the script being called without any command.'''

        # pylint: disable=no-self-use

        return NotImplemented
