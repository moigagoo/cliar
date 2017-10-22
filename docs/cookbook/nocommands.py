from cliar import Cliar


class NoCommands(Cliar):
    '''This is a CLI without commands; the script itself is a command.

    Calling the script will print this important message.

    Add "-c" for more dramatism.
    '''

    def _root(self, capitalize=False):
        line = 'The script itself is a command'

        if capitalize:
            line = line.upper()

        print(line)


if __name__ == '__main__':
    NoCommands().parse()
