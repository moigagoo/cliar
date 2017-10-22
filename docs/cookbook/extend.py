from cliar import Cliar


class Basic(Cliar):
    '''Basic CLI with two commands.'''

    def start(self, server):
        '''Start a server'''

        print('> Starting %s' % server)

    def stop(self, server):
        '''Stop a server'''

        print('> Stopping %s' % server)


class Extended(Basic):
    '''Extended CLI that overrides one basic command and add one new one.'''

    def start(self, server):
        '''Start a server with additional stuff before and after.'''

        print('>> Do stuff before server start')
        super(Extended, self).start(server)
        print('>> Do stuff after server start')

    def restart(self, server):
        '''Restart a server = stop + start'''

        print('>> Restarting %s:' % server)
        self.stop(server)
        self.start(server)


if __name__ == '__main__':
    Extended().parse()
