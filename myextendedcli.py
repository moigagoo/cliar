from mycli import MyCLI

class MyExtendedCLI(MyCLI):
    '''This is the extended version of my command-line interface'''

    def goodbye(self):
        print('Good bye, and happy hacking!')

if __name__ == '__main__':
    MyExtendedCLI()