from sys import version_info


if version_info.major == 3:
    from .py3.cliar import *

elif version_info.major == 2:
    from .py2.cliar import *
