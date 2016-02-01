from cliar import CLI


class TypeChecking(CLI):
    '''This is a CLI with one command
    that has one positional arg of type int.
    '''

    def square(self, n:int):
        '''Square a given number'''

        print('%d squared is %d' % (n, n**2))


if __name__ == '__main__':
    TypeChecking().parse()