************
Optional Arg
************

:download:`Download source <optional.py>`

.. literalinclude:: optional.py

Usage:

.. code-block:: bash

    $ python optional.py -h
    usage: optional.py [-h] {hello} ...

    This is a CLI with one command that has an optional arg.

    optional arguments:
      -h, --help  show this help message and exit

    commands:
      {hello}     available commands
        hello     Say hello to NAME; if no name is give, say hello to Guido

    $ python optional.py hello -h
    usage: optional.py hello [-h] [-name NAME]

    optional arguments:
      -h, --help  show this help message and exit
      -name NAME

    $ python optional.py hello
    Hello, Guido

    $ python optional.py hello -name John
    Hello, John

    $ python optional.py hello -n Sandy
    Hello, Sandy
