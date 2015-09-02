from cliar import CLI


class SimpleCLI(CLI):
    '''This is a CLI with one command that has one positional arg.'''

    def hello(self, name):
        '''Say hello to NAME'''

        print('Hello, %s' % name)


if __name__ == '__main__':
    SimpleCLI()