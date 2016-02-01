from cliar import CLI


class Openfile(CLI):
    '''This CLI has a command that takes a filepath
    and attempts to open it on the fly.
    '''

    def find_word(self, file:open, word:str):
        '''Find WORD in FILE'''

        if word in file.read():
            print('Here it is!')
        else:
            print('Nope, not here')


if __name__ == '__main__':
    Openfile().parse()