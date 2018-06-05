from math import pi, e, log
from typing import List

from cliar import Cliar, add_aliases, set_help, ignore, set_name, set_arg_map, set_metavars


class Math(Cliar):
    '''Basic math operations.'''

    @set_help({'x': 'First operand', 'y': 'Second operand'})
    def add(self, x: int, y: int):
        '''Add two numbers.'''

        print(x+y)

    def power(self, x: int, power=2):
        print(x**power)

    def pi(self):
        print(pi)

    def echo(self, message: str):
        print(message)

    @add_aliases(['sum', 'plus'])
    def summ(self, numbers: List[int]):
        print(sum(numbers))

    def avg(self, numbers: List[float] = [1, 2, 3]):
        print(sum(numbers)/len(numbers))

    def sumfile(self, file: open):
        numbers = (float(line) for line in file.readlines())
        print(sum(numbers))

    @ignore
    def calculate_factorial(self, n: int, acc: int):
        if n == 0:
            return acc

        elif n > 0:
            return self.calculate_factorial(n-1, acc*n)

        else:
            raise ValueError('Cannot calculate factorial of negative number.')

    @set_name('fac')
    def factorial(self, n: int):
        print(self.calculate_factorial(n, 1))

    @set_arg_map({'base': 'to'})
    @set_metavars({'base': 'BASE'})
    def log(self, x: float, base=e):
        print(log(x, base))

    def _root(self, version=False):
        if version:
            print('0.1.0')

        else:
            print('Welcome to math!')


if __name__ == '__main__':
    Math().parse()
