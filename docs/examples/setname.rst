****************
Set Command Name
****************

.. note:: This example works in Python 3 only. To make it work in Python 2, remove ``:int``.

:download:`Download source <setname.py>`

.. literalinclude:: setname.py

Usage:

.. code-block:: bash

    $ python setname.py -h
    usage: setname.py [-h] {get-random} ...

    This CLI has a command that is called differently than its handler method.

    optional arguments:
      -h, --help    show this help message and exit

    commands:
      {get-random}  available commands
        get-random  Get a random number between FROM_NUMBER and TO_NUMBER

    $ python setname.py get-random -h
    usage: setname.py get-random [-h] from_number to_number

    positional arguments:
      from_number
      to_number

    optional arguments:
      -h, --help   show this help message and exit

    $ python setname.py get-random 1 10
    Here is a random number between 1 and 10: 6

    $ python setname.py get-random 1
    usage: setname.py get-random [-h] from_number to_number
    setname.py get-random: error: the following arguments are required: to_number

    $ python setname.py get-random 1 foo
    usage: setname.py get-random [-h] from_number to_number
    setname.py get-random: error: argument to_number: invalid int value: 'foo'
