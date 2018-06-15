from math import factorial, tau, pi

from cliar import Cliar, set_help, set_metavars, set_arg_map, add_aliases, set_name, ignore


class Greeter(Cliar):
    '''Greeter app created with in Cliar.'''

    def _get_tau_value(self):
        return tau

    @ignore
    def get_pi_value(self):
        return pi

    def constants(self):
        print(f'τ = {self._get_tau_value()}')
        print(f'π = {self.get_pi_value()}')

    @set_name('factorial')
    def calculate_factorial(self, n: int):
        print(f'n! = {factorial(n)}')

    @add_aliases(['mientras', 'пока'])  # Yes you can use non-Latin characters
    def goodbye(self, name):
        '''Say goodbye'''

        print(f'Goodbye {name}!')

    @set_arg_map({'n': 'repeat'})
    @set_metavars({'name': 'NAME'})
    @set_help({'name': 'The greetee', 'shout': 'Set to shout the greeting'})
    def hello(self, name, n=1, shout=False):
        '''Say hello.'''

        greeting = f'Hello {name}!'

        for _ in range(n):
            if shout:
                print(greeting.upper())
            else:
                print(greeting)


if __name__ == '__main__':
    greeter = Greeter()
    greeter.parse()
