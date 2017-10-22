from argparse import ArgumentParser, RawTextHelpFormatter
from inspect import signature, getmembers, ismethod

from collections import OrderedDict

from typing import Callable, List, Iterable, Dict


def set_metavars(metavar_map: Dict[str, str]) -> Callable:
    def decorator(handler: Callable) -> Callable:
        handler._metavar_map = metavar_map
        return handler

    return decorator


def set_arg_map(arg_map: Dict[str, str]) -> Callable:
    '''Override mapping from handler params to commandline args.

    :param arg_map: mapping from handler param names to arg names
    '''

    def decorator(handler: Callable) -> Callable:
        '''Decorator returning command handler with a custom arg map.'''

        handler._arg_map = arg_map
        return handler

    return decorator


def set_name(name: str) -> Callable:
    '''Override the name of the CLI command. By default, commands are called the same
    as their corresponding handlers.

    :param name: new command name
    '''

    if name == '':
        raise NameError('Command name cannot be empty')

    def decorator(handler: Callable) -> Callable:
        '''Decorator returning command handler with a custom command name.'''

        handler._command_name = name
        return handler

    return decorator


def add_aliases(aliases: List[str]) -> Callable:
    '''Add command aliases.

    :param aliases: list of aliases
    '''

    def decorator(handler: Callable) -> Callable:
        '''Decorator returning command handler with a list of aliases set for its command.'''

        handler._command_aliases = aliases
        return handler

    return decorator


def ignore(handler: Callable) -> Callable:
    '''Exclude a method from being converted into a command.

    :param method: method to ignore
    '''

    handler._ignore = True
    return handler


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

        self.args = self._get_args()

    def _get_args(self) -> OrderedDict:
        '''Get command arguments from the parsed signature of its handler.'''

        args = OrderedDict()

        handler_signature = signature(self.handler)

        for param_name, param_data in handler_signature.parameters.items():
            arg = _Arg()

            if param_data.annotation is not param_data.empty:
                arg.type = param_data.annotation

            if param_data.default is not param_data.empty:
                arg.default = param_data.default

                if not arg.type:
                    arg.type = type(arg.default)

            if arg.type == bool:
                if arg.default is True:
                    arg.action = 'store_false'

                elif arg.default is False:
                    arg.action = 'store_true'

            elif arg.type in (list, tuple):
                if arg.default:
                    arg.nargs = '*'

                else:
                    arg.nargs = '+'

            if not arg.action and param_name in self.metavar_map:
                arg.metavar = self.metavar_map[param_name]

            if param_name not in self.arg_map:
                self.arg_map[param_name] = param_name.replace('_', '-')

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

    def _register_arg(self, command_parser: ArgumentParser, arg_name: str, arg_data: _Arg):
        '''Register an arg in the specified argparser.

        :param command_parser: global argparser or a subparser corresponding to a CLI command
        :param str arg_name: handler param name without prefixing dashes
        :param arg_data: arg type, default value, and action
        '''

        if arg_data.default is None:
            arg_prefixed_names = [arg_name]

        else:
            arg_prefixed_names = ['-'+arg_name[0], '--'+arg_name]

        if arg_data.action:
            command_parser.add_argument(
                *arg_prefixed_names,
                default=arg_data.default,
                action=arg_data.action
            )

        elif arg_data.nargs:
            command_parser.add_argument(
                *arg_prefixed_names,
                default=arg_data.default,
                nargs=arg_data.nargs,
                metavar=arg_data.metavar
            )

        else:
            command_parser.add_argument(
                *arg_prefixed_names,
                type=arg_data.type,
                default=arg_data.default,
                metavar=arg_data.metavar
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

        root_args = {arg: vars(args)[arg] for arg in self.root_command.args}

        inverse_root_arg_map = {arg: param for param, arg in self.root_command.arg_map.items()}

        self.root_command.handler(
            **{inverse_root_arg_map[arg]: value for arg, value in root_args.items()}
        )

        if self._commands:
            command = self._commands.get(args.command)

            if command:
                command_args = {arg: vars(args)[arg.replace('-', '_')] for arg in command.args}

                inverse_arg_map = {arg: param for param, arg in command.arg_map.items()}

                command.handler(
                    **{inverse_arg_map[arg]: value for arg, value in command_args.items()}
                )

            else:
                self._parser.print_help()


    def _root(self):
        '''The root command, which corresponds to the class itself.

        Use it to define global args.
        '''

        pass
