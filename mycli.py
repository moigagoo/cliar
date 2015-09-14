from cliar import CLI

class MyCLI(CLI):
    '''This is my own command-line interface built with Cliar'''

    def start(self, awesome=False):
        '''This is a command in my CLI. Apparently, it starts something.'''

        print('Started...')

        if awesome:
            print("...and it's awesome!")

        else:
            print('...with no awesomeness.')

    def say(self, word:str, n:int=1):
        '''This command says stuff.'''

        if self.capitalize:
            word = word.upper()

        for _ in range(n):
            print(word)

    def _root(self, capitalize=False):
        self.capitalize = capitalize

        if capitalize:
            print('Everything you say will be in CAPS.')

if __name__ == '__main__':
    MyCLI().parse()
