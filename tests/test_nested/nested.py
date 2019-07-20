from cliar import Cliar


class Remote(Cliar):
    '''Remote help.'''

    def _root(self):
        print('Remote root.')

    def add(self, name: str):
        '''Remote add help.'''
        print(f'Adding remote {name}')

    def show(self):
        '''Remote show help.'''
        print('Show all remotes')


class Git(Cliar):
    '''Git help.'''

    remote = Remote

    def _root(self):
        print('Git root.')

    def branch(self, name):
        '''Git branch help.'''
        print(f'Setting branch to {name}')

Git().parse()
