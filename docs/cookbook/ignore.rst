**************************************
Do Not Convert a Method into a Command
**************************************


:download:`Download source <ignore.py>`

.. literalinclude:: ignore.py

Usage:

.. code-block:: bash

    $ python ignore.py -h
    usage: ignore.py [-h] {square} ...

    This CLI has a method that is not converted into a command.

    optional arguments:
      -h, --help  show this help message and exit

    commands:
      {square}    available commands
        square    Return a square of a number

    $ python ignore.py square -h
    usage: ignore.py square [-h] num

    positional arguments:
      num

    optional arguments:
      -h, --help  show this help message and exit

    $ python ignore.py square 13
    Here is your number squared: 169

    $ python ignore.py sqr 13
    usage: ignore.py [-h] {square} ...
    ignore.py: error: argument command: invalid choice: 'sqr' (choose from 'square')