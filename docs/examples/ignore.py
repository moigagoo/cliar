from cliar import CLI, ignore

from random import randint


class Ignore(CLI):
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
    Ignore()