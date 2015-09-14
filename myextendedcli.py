from cliar import add_aliases
from mycli import MyCLI

class MyExtendedCLI(MyCLI):
    '''This is the extended version of my command-line interface'''

    @add_aliases(['gb'])
    def goodbye(self):
        print('Good bye, and happy hacking!')

if __name__ == '__main__':
    MyExtendedCLI().parse()