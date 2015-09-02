************
Simplest CLI
************

:download:`Download source <simplest.py>`

.. literalinclude:: simplest.py

Usage:

.. code-block:: bash

    $ python simplest.py -h
    usage: simplest.py [-h] {hello} ...

    This is a CLI with one command that has one positional arg.

    optional arguments:
      -h, --help  show this help message and exit

    commands:
      {hello}     available commands
        hello     Say hello to NAME

    $ python simplest.py hello -h
    usage: simplest.py hello [-h] name

    positional arguments:
      name

    optional arguments:
      -h, --help  show this help message and exit

    $ python simplest.py hello Guido
    Hello, Guido

    $ python simplest.py hello
    usage: simplest.py hello [-h] name
    simplest.py hello: error: the following arguments are required: name