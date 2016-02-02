from sys import version_info


if version_info.major < 3:
    from .legacy.cliar import *

elif version_info.major == 3 and version_info.minor < 3:
    raise NotImplementedError('Python 3.1 and 3.2 is not supported.')

else:
    from .modern.cliar import *
