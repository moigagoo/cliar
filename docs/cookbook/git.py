from cliar import Cliar


class Git(Cliar):
    '''This is a Git CLI clone.

    It doesn't actually do stuff, just imitates 2 git commands.
    '''

    def _root(self, config='~/.gitconfig'):
        print('The config is: %s' % config)

    def clone(self, repo, dir='.'):
        '''Clone REPO to DIR'''

        print('Cloning the repo: %s. Destination: %s' % (repo, dir))

    def checkout(self, branch, force=False, quiet=False):
        '''Checkout to BRANCH.

        Use "-f" for force and "-q" for quiet.
        '''

        print('Checking out to %s' % branch)

        if force:
            print('Forced checkout')

        if quiet:
            print('Quiet checkout')


if __name__ == '__main__':
    Git().parse()
