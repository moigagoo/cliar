**************
Positional Arg
**************

:download:`Download source <positional.py>`

.. literalinclude:: positional.py

Usage:

.. code-block:: bash

    $ python positional.py -h
    usage: positional.py [-h] {hello} ...

    This is a CLI with one command that has one positional arg.

    optional arguments:
      -h, --help  show this help message and exit

    commands:
      {hello}     available commands
        hello     Say hello to NAME

    $ python positional.py hello -h
    usage: positional.py hello [-h] name

    positional arguments:
      name

    optional arguments:
      -h, --help  show this help message and exit

    $ python positional.py hello Guido
    Hello, Guido

    $ python positional.py hello
    usage: positional.py hello [-h] name
    positional.py hello: error: the following arguments are required: name