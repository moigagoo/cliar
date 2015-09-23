from sys import exit

from argparse import ArgumentParser, RawTextHelpFormatter
from inspect import signature, getmembers, ismethod

from collections import OrderedDict


def set_name(name):
    '''Set the name of the CLI command if you don't like it being the same as the corresponding method.

    :param name: new command name

    :returns: a decorator that returns a method with the updated name
    '''

    if not name:
        raise NameError('Command name cannot be empty')

    def decorator(method):
        method._command_name = name
        return method

    return decorator


def add_aliases(aliases):
    '''Add command aliases.

    :param aliases: list of aliases

    :returns: a decorator that returns a method with the new aliases list
    '''

    def decorator(method):
        method._command_aliases = aliases
        return method

    return decorator


def ignore(method):
    '''Exclude a method from being converted into a CLI command.
    
    This decorator adds the ``_ignore`` attribute to the method.
    
    Methods with this attribute are skipped when commands are registered.

    :param method: method to ignore

    :returns: modified method
    '''

    method._ignore = True
    return method


class _Arg:
    '''CLI command argument.

    Its attributes correspond to the homonymous params of the ``add_argument`` function.
    '''

    def __init__(self):
        self.type = None
        self.default = None
        self.action = None
        self.nargs = None


class _Command:
    '''CLI command.

    A wrapper around a method that adds a few hidden attributes.
    
    Command args correspond to method params.
    '''

    def __init__(self, handler):
        self.handler = handler

        self.args = OrderedDict()
        self._add_args()

        if hasattr(handler, '_command_name'):
            self.name = handler._command_name
        else:
            self.name = handler.__name__

        if hasattr(handler, '_command_aliases'):
            self.aliases = handler._command_aliases
        else:
            self.aliases = []

    def _add_args(self):
        '''Parse method's signature to add CLI command's arguments.'''

        handler_signature = signature(self.handler)

        for param_name, param_data in list(handler_signature.parameters.items()):
            arg = _Arg()

            if param_data.annotation is not param_data.empty:
                arg.type = param_data.annotation

            if param_data.default is not param_data.empty:
                arg.default = param_data.default

                if not arg.type:
                    arg.type = type(arg.default)

            if arg.type == bool:
                if arg.default == True:
                    arg.action = 'store_false'

                elif arg.default == False:
                    arg.action = 'store_true'

            elif arg.type in (list, tuple):
                if arg.default:
                    arg.nargs = '*'

                else:
                    arg.nargs = '+'

            self.args[param_name] = arg


class CLI:
    '''Subclass from this class to create your own CLI.
    
    Every method without an underscore is mapped to a CLI command.

    The special ``_root`` method corresponds to the script itself.
    '''

    def __init__(self):
        self._parser = ArgumentParser(
            description=self.__doc__,
            formatter_class=RawTextHelpFormatter
        )

        self._register_root_args()

        self._command_parsers = self._parser.add_subparsers(
            dest='command',
            title='commands',
            help='Available commands:'
        )

        self._commands = {}
        self._register_commands()

    def _register_root_args(self):
        '''Register root args (i.e. params of ``self._root``) in the global argparser.'''

        self.root_command = _Command(self._root)

        for arg_name, arg_data in self.root_command.args.items():
            self._register_arg(self._parser, arg_name, arg_data)

    def _register_arg(self, command_parser, arg_name, arg_data):
        '''Register an arg in the specified argparser.

        :param command_parser: global argparser or a subparser corresponding to a CLI command
        :param arg_name: arg name without prefixing dashes
        :param arg_data: arg type, default value, and action
        '''

        if arg_data.default is None:
            arg_prefix = ''

        else:
            arg_prefix = '-'

        if arg_data.action:
            command_parser.add_argument(
                arg_prefix + arg_name,
                default=arg_data.default,
                action=arg_data.action
            )

        elif arg_data.nargs:
            command_parser.add_argument(
                arg_prefix + arg_name,
                default=arg_data.default,
                nargs=arg_data.nargs
            )

        else:
            command_parser.add_argument(
                arg_prefix + arg_name,
                type=arg_data.type,
                default=arg_data.default
            )

    def _register_commands(self):
        '''Create parsers for all non-root commands.'''

        handlers = (
            method 
            for method_name, method in getmembers(self, predicate=ismethod)
            if not method_name.startswith('_') and not hasattr(method,'_ignore')
        )

        for handler in handlers:
            command = _Command(handler)

            command_parser = self._command_parsers.add_parser(
                command.name,
                help=handler.__doc__.splitlines()[0] if handler.__doc__ else '',
                description=handler.__doc__,
                aliases=command.aliases
            )

            for arg_name, arg_data in command.args.items():
                self._register_arg(command_parser, arg_name, arg_data)

            self._commands[command.name] = command

            for alias in command.aliases:
                self._commands[alias] = command

    @ignore
    def parse(self):
        '''Parse command line args, i.e. launch the CLI.'''

        args = self._parser.parse_args()

        root_args = {root_arg: vars(args)[root_arg] for root_arg in self.root_command.args}
        self.root_command.handler(**root_args)

        command = self._commands.get(args.command)

        if command and self._commands:
            command_args = {command_arg: vars(args)[command_arg] for command_arg in command.args}
            command.handler(**command_args)

        elif self._commands:
            self._parser.print_help()


    def _root(self):
        '''The root command. Use to declare and process global command-line args.'''

        pass
