****************
Arg Type Casting
****************

:download:`Download source <typecasting.py>`

.. literalinclude:: typecasting.py

Usage:

.. code-block:: bash

    $ python typecasting.py -h
    usage: typecasting.py [-h] {square} ...

    This is a CLI with one command that has one positional arg of type int.

    optional arguments:
      -h, --help  show this help message and exit

    commands:
      {square}    available commands
        square    Square a given number

    $ python typecasting.py square -h
    usage: typecasting.py square [-h] n

    positional arguments:
      n

    optional arguments:
      -h, --help  show this help message and exit

    $ python typecasting.py square 3
    3 squared is 9

    $ python type_checking.py square foo
    usage: typecasting.py square [-h] n
    type_checking.py square: error: argument n: invalid int value: 'foo'

    $ python type_checking.py square 3.14
    usage: typecasting.py square [-h] n
    type_checking.py square: error: argument n: invalid int value: '3.14'