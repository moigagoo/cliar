from typing import Callable, List, Dict


# pylint: disable=too-few-public-methods,protected-access


def set_help(help_map: Dict[str, str]) -> Callable:
    '''Set help messages for arguments.

    :param help_map: mapping from handler param names to help messages
    '''
    def decorator(handler: Callable) -> Callable:
        '''Decorator returning command handler with a help message map.'''

        handler._help_map = help_map
        return handler

    return decorator


def set_metavars(metavar_map: Dict[str, str]) -> Callable:
    '''Override default metavars for arguments.

    By default, metavars are generated from arg names: ``foo`` → ``FOO``, `--bar`` → ``BAR``.

    :param metavar_map: mapping from handler param names to metavars
    '''
    def decorator(handler: Callable) -> Callable:
        '''Decorator returning command handler with a custom metavar map.'''

        handler._metavar_map = metavar_map
        return handler

    return decorator


def set_arg_map(arg_map: Dict[str, str]) -> Callable:
    '''Override mapping from handler params to commandline args.

    Be default, param names are used as arg names with underscores replaced with dashes.

    :param arg_map: mapping from handler param names to arg names
    '''

    def decorator(handler: Callable) -> Callable:
        '''Decorator returning command handler with a custom arg map.'''

        handler._arg_map = arg_map
        return handler

    return decorator


def set_sharg_map(sharg_map: Dict[str, str]) -> Callable:
    '''Override mapping from handler params to short commandline arg names.

    Be default, the first character of arg names are used as short arg names.

    :param arg_map: mapping from handler param names to short arg names
    '''

    def decorator(handler: Callable) -> Callable:
        '''Decorator returning command handler with a custom shaarg map.'''

        handler._sharg_map = sharg_map
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
