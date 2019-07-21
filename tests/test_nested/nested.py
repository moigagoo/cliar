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
        print('Showing all remotes')

class Feature(Cliar):
    '''Feature help.'''

    def start(self, name: str):
        '''Feature start help.'''
        print(f'Starting feature {name}')

class Flow(Cliar):
    '''Flow help.'''

    feature = Feature

class Git(Cliar):
    '''Git help.'''

    remote = Remote
    flow = Flow

    def _root(self):
        print('Git root.')

    def branch(self, name):
        '''Git branch help.'''
        print(f'Setting branch to {name}')

Git().parse()
