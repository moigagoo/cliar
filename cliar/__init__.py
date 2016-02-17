from sys import version_info


if version_info.major < 3:
    from .legacy.cliar import *
    from .legacy.cliar import _Arg, _Command

elif version_info.major == 3 and version_info.minor < 3:
    raise NotImplementedError('Python 3.1 and 3.2 is not supported.')

else:
    from .modern.cliar import *
    from .modern.cliar import _Arg, _Command

__all__ = ['CLI', '_Command', '_Arg', 'add_aliases', 'set_name', 'ignore']