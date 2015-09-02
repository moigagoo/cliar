*****************
Arg Type Checking
*****************

.. note:: This examples works in Python 3 only.

:download:`Download source <typechecking.py>`

.. literalinclude:: typechecking.py

Usage:

.. code-block:: bash

    $ python typechecking.py -h
    usage: type_checking.py [-h] {square} ...

    This is a CLI with one command that has one positional arg of type int.

    optional arguments:
      -h, --help  show this help message and exit

    commands:
      {square}    available commands
        square    Square a given number

    $ python typechecking.py square -h
    usage: type_checking.py square [-h] n

    positional arguments:
      n

    optional arguments:
      -h, --help  show this help message and exit

    $ python typechecking.py square 3
    3 squared is 9

    $ python type_checking.py square foo
    usage: type_checking.py square [-h] n
    type_checking.py square: error: argument n: invalid int value: 'foo'

    $ python type_checking.py square 3.14
    usage: type_checking.py square [-h] n
    type_checking.py square: error: argument n: invalid int value: '3.14'