from math import pi, e, log
from typing import List

from cliar import Cliar, set_name


class NoRoot(Cliar):
    '''Basic math operations.'''

    def add(self, x: int, y: int):
        print(x+y)


if __name__ == '__main__':
    NoRoot().parse()
