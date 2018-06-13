from cliar import Cliar, set_help, set_metavars


class Greeter(Cliar):
    '''Greeter app created with in Cliar.'''

    @set_help({'name': 'The greetee', 'shout': 'Set to shout the greeting'})
    @set_metavars({'name': 'NAME'})
    def hello(self, name, shout=False):
        '''Say hello.'''

        greeting = f'Hello {name}!'

        if shout:
            print(greeting.upper())
        else:
            print(greeting)


if __name__ == '__main__':
    greeter = Greeter()
    greeter.parse()
