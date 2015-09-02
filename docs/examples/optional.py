from cliar import CLI


class OptionalArg(CLI):
    '''This is a CLI with one command that has an optional arg.'''

    def hello(self, name='Guido'):
        '''Say hello to NAME; if no name is give, say hello to Guido'''

        print('Hello, %s' % name)


if __name__ == '__main__':
    OptionalArg()