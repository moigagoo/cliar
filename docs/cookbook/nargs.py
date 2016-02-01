from cliar import CLI


class Nargs(CLI):
    '''This is a CLI with commands
    that accept a sequence of values
    for a single arg.
    '''

    def hello(self, names:list=['Mary', 'John']):
        '''Say hello to people'''

        for name in names:
            print('Hello, %s!' % name)


    def sum(self, numbers:tuple):
        '''Sum all the given numbers'''

        result = 0

        for number in numbers:
            result += int(number)

        print('The sum is %d' % result)


if __name__ == '__main__':
    Nargs().parse()