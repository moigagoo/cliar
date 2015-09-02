*******************
Add Command Aliases
*******************

.. note:: This examples works in Python 3 only.


:download:`Download source <aliases.py>`

.. literalinclude:: aliases.py

Usage:

.. code-block:: bash

    $ python aliases.py -h
    usage: aliases.py [-h] {get-random,gr,randint} ...

    This CLI has a command that is called differently than its handler method and
    has aliases.

    optional arguments:
      -h, --help            show this help message and exit

    commands:
      {get-random,gr,randint}
                            available commands
        get-random (gr, randint)

    $ python aliases.py gr -h
    usage: aliases.py get-random [-h] from_number to_number

    positional arguments:
      from_number
      to_number

    optional arguments:
      -h, --help   show this help message and exit

    $ python aliases.py gr 1 10
    Here is a random number between 1 and 10: 8

    $ python aliases.py randint 1 10
    Here is a random number between 1 and 10: 4

    $ python aliases.py get-random 1 10
    Here is a random number between 1 and 10: 9