﻿from cliar import Cliar, set_name

from random import randint


class SetName(Cliar):
    '''This CLI has a command that is called
    differently than its handler method.
    '''

    @set_name('get-random')
    def get_random_number(self, from_number: int, to_number: int):
        '''Get a random number between FROM_NUMBER and TO_NUMBER'''

        print(
            'Here is a random number between %d and %d: %d' %
            (from_number, to_number, randint(from_number, to_number))
        )


if __name__ == '__main__':
    SetName().parse()