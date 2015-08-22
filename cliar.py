'''Cliar (read as "clear") is a thin wrapper around argparse that lets you create extendable command-line interfaces in a quick and clear way.
'''


__title__ = 'cliar'
__description__ = 'Build command-line interfaces quickly and clearly'
__version__ = '1.0.0'
__author__ = 'Konstantin Molchanov'
__author_email__ = 'moigagoo@live.com'
__license__ = 'MIT'

from sys import exit

from argparse import ArgumentParser
from inspect import signature

from collections import OrderedDict


def set_name(name):
    '''Set function's ``__name__`` attribute.
    
    Used as ``@set_name('new_name')`` to name a CLI command differently then its corresponding method.

    :param name: new value for the ``__name__`` attribute

    :returns: a decorator that returns a function with the new ``__name__`` attribute value
    '''

    if not name:
        raise NameError('Command name cannot be empty')

    def decorator(func):
        func.__name__ = name
        return func

    return decorator


class _Arg:
    '''CLI command argument.
    
    Its attributes correspond to the homonymous params of the ``add_argument`` function.
    '''

    def __init__(self):
        self.type = None
        self.default = None
        self.action = None


class _Command:
    '''CLI command.
    
    Basically, a wrapper around a method. Command's args correspond to method's params.
    '''

    def __init__(self, handler):
        self.handler = handler

        self.args = OrderedDict()
        self._add_args()

    def _add_args(self):
        '''Parse method's signature to add CLI command's arguments.'''

        handler_signature = signature(self.handler)

        for param_name, param_data in list(handler_signature.parameters.items())[1:]:
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

            self.args[param_name] = arg


class CLI:
    '''Cliar command line interface.'''

    def __init__(self):
        self._parser = ArgumentParser(description=self.__doc__)

        self._register_root_args()

        self._command_parsers = self._parser.add_subparsers(
            dest='command',
            title='commands',
            help='available commands'
        )

        self._commands = {}
        self._register_commands()

        self._parse()

    def _register_root_args(self):
        '''Register root args (i.e. params of ``self._root``) in the global argparser.'''

        self.root_command = _Command(self.__class__._root)

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

        else:
            command_parser.add_argument(
                arg_prefix + arg_name,
                type=arg_data.type,
                default=arg_data.default
            )

    def _register_commands(self):
        '''Create parsers for all non-root commands.'''

        for parent in self.__class__.mro():
            handlers = (
                method 
                for method_name, method in parent.__dict__.items()
                if not method_name.startswith('_')
            )

            for handler in handlers:
                command = _Command(handler)

                command_parser = self._command_parsers.add_parser(handler.__name__, help=handler.__doc__)

                for arg_name, arg_data in command.args.items():
                    self._register_arg(command_parser, arg_name, arg_data)

                self._commands[handler.__name__] = command

    def _parse(self):
        '''Parse command line args, i.e. launch the CLI.'''

        args = self._parser.parse_args()

        root_args = {root_arg: vars(args)[root_arg] for root_arg in self.root_command.args}
        self.root_command.handler(self, **root_args)

        command = self._commands.get(args.command)

        if command and self._commands:
            command_args = {command_arg: vars(args)[command_arg] for command_arg in command.args}
            command.handler(self, **command_args)

        elif self._commands:
            self._parser.print_help()


    def _root(self):
        '''The root command. Use to declare and process global command-line args.'''

        pass