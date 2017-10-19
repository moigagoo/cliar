from cliar import Cliar, ignore

from random import randint


class Ignore(Cliar):
    '''This CLI has a method that is not
    converted into a command.
    '''

    @ignore
    def sqr(self, x):
        return x ** 2

    def square(self, num:int):
        '''Return a square of a number'''

        print('Here is your number squared: %d' % self.sqr(num))


if __name__ == '__main__':
    Ignore().parse()