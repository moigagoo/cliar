from argparse import ArgumentParser, RawTextHelpFormatter
from asyncio import get_event_loop
from inspect import signature, getmembers, ismethod, isclass, iscoroutine
from collections import OrderedDict
from typing import List, Iterable, Callable, Set, Type, get_type_hints

from .utils import ignore


# pylint: disable=too-few-public-methods, protected-access, too-many-instance-attributes


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

        self.arg_map = {}
        if hasattr(handler, '_arg_map'):
            self.arg_map = handler._arg_map

        self.sharg_map = {}
        if hasattr(handler, '_sharg_map'):
            self.sharg_map = handler._sharg_map

        self.metavar_map = {}
        if hasattr(handler, '_metavar_map'):
            self.metavar_map = handler._metavar_map

        self.name = handler.__name__.replace('_', '-')
        if hasattr(handler, '_command_name'):
            self.name = handler._command_name

        self.aliases = []
        if hasattr(handler, '_command_aliases'):
            self.aliases = handler._command_aliases

        self.help_map = {}
        if hasattr(handler, '_help_map'):
            self.help_map = handler._help_map

        self.formatter_class = RawTextHelpFormatter
        if hasattr(handler, '_formatter_class'):
            self.formatter_class = handler._formatter_class

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

            arg.type = get_type_hints(self.handler).get(param_name)

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
    -   ``self._root`` corresponds to the root command. Use it to define global args.
    '''

    def __init__(
            self,
            parser_name: str or None = None,
            parent: Type['Cliar'] or None = None
        ):
        if parent:
            self._parser = parent._command_parsers.add_parser(
                parser_name,
                description=self.__doc__,
                help=self.__doc__,
                formatter_class=RawTextHelpFormatter
            )
        else:
            self._parser = ArgumentParser(
                description=self.__doc__,
                formatter_class=RawTextHelpFormatter
            )

        self._register_root_args()

        self._commands = {}
        self._subclis = []

        handlers, subclis = self._get_handlers(), self._get_subclis()

        if handlers or subclis:
            self._command_parsers = self._parser.add_subparsers(
                title='commands'
            )
            self._register_commands(handlers)

            for subcli_name, subcli_class in subclis.items():
                self._subclis.append(subcli_class(subcli_name, self))

        self.global_args = {}

    def _register_root_args(self):
        '''Register root args, i.e. params of ``self._root``, in the global argparser.'''

        self.root_command = _Command(self._root)
        self._parser.set_defaults(_command=self.root_command)

        for arg_name, arg in self.root_command.args.items():
            self._register_arg(self._parser, arg_name, arg)

    @staticmethod
    def _register_arg(command_parser: ArgumentParser, arg_name: str, arg: _Arg):
        '''Register an arg in the specified argparser.

        :param command_parser: global argparser or a subparser corresponding to a CLI command
        :param str arg_name: handler param name without prefixing dashes
        :param arg: arg type, default value, and action
        '''

        if arg.default is None:
            arg_prefixed_names = []

        elif arg.short_name:
            arg_prefixed_names = ['-'+arg.short_name, '--'+arg_name]

        else:
            arg_prefixed_names = ['--'+arg_name]

        if arg.action:
            command_parser.add_argument(
                *arg_prefixed_names,
                dest=arg_name,
                default=arg.default,
                action=arg.action,
                help=arg.help
            )

        elif arg.nargs:
            command_parser.add_argument(
                *arg_prefixed_names,
                dest=arg_name,
                type=arg.type,
                default=arg.default,
                nargs=arg.nargs,
                metavar=arg.metavar,
                help=arg.help
            )

        else:
            command_parser.add_argument(
                *arg_prefixed_names,
                dest=arg_name,
                type=arg.type,
                default=arg.default,
                metavar=arg.metavar,
                help=arg.help
            )

    def _get_handlers(self) -> List[Callable]:
        '''Get all handlers except ``self._root``.'''

        return (
            method
            for method_name, method in getmembers(self, predicate=ismethod)
            if not method_name.startswith('_') and not hasattr(method, '_ignore')
        )

    def _get_subclis(self):
        condition = lambda m: isclass(m) and issubclass(m, Cliar)

        return {
            member_name: member
            for member_name, member in getmembers(self, predicate=condition)
            if not member_name.startswith('_')
        }

    def _register_commands(self, handlers: Iterable[Callable]):
        '''Create parsers for commands from handlers (except for ``self._root``).'''

        for handler in handlers:
            command = _Command(handler)

            command_parser = self._command_parsers.add_parser(
                command.name,
                help=handler.__doc__.splitlines()[0] if handler.__doc__ else '',
                description=handler.__doc__,
                formatter_class=command.formatter_class,
                aliases=command.aliases
            )
            command_parser.set_defaults(_command=command)

            for arg_name, arg in command.args.items():
                self._register_arg(command_parser, arg_name, arg)

            self._commands[command.name] = command

            for alias in command.aliases:
                self._commands[alias] = command

    @ignore
    def parse(self):
        '''Parse commandline input, i.e. launch the CLI.'''

        args = self._parser.parse_args()

        command = args._command
        command_args = {arg: vars(args)[arg] for arg in command.args}
        inverse_arg_map = {arg: param for param, arg in command.arg_map.items()}
        handler_args = {inverse_arg_map[arg]: value for arg, value in command_args.items()}

        self.global_args = {
            arg: value
            for arg, value in vars(args).items()
            if arg not in ['_command', *command_args.keys()]
        }
        for subcli in self._subclis:
            subcli.global_args = self.global_args

        result = command.handler(**handler_args)

        if iscoroutine(result):
            result = get_event_loop().run_until_complete(result)

        if result == NotImplemented:
            command.handler.__self__._parser.print_help()

    def _root(self):
        '''The root command, which corresponds to the script being called without any command.'''

        # pylint: disable=no-self-use

        return NotImplemented
