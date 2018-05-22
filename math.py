from math import pi
from typing import List

from cliar import Cliar


class Positional(Cliar):
    def add(self, x: int, y: int):
        print(x+y)

    def power(self, x: int, power=2):
        print(x**power)

    def pi(self):
        print(pi)

    def summ(self, numbers: List[int]):
        print(sum(numbers))

    def avg(self, numbers: List[float] = [1, 2, 3]):
        print(sum(numbers)/len(numbers))

    def sumfile(self, file: open):
        numbers = (float(line) for line in file.readlines())
        print(sum(numbers))

    def _root(self, version=False):
        if version:
            print('0.1.0')

        else:
            print('Welcome to math!')


if __name__ == '__main__':
    Positional().parse()
