********************************
Multiple Values for a Single Arg
********************************

Annotate the param type as ``list`` or ``tuple`` to make it collect multiple values into a single arg.

Since Python 2 doesn't have function annotations, use an empty list or tuple to define a required sequence of values::

    def sum(self, numbers=()):
        ...

:download:`Download source <nargs.py>`

.. literalinclude:: nargs.py

Usage:

.. code-block:: bash

    $ python nargs.py -h
    usage: nargs.py [-h] {hello,sum} ...

    This is a CLI with commands that accept a sequence of values for a single arg.

    optional arguments:
      -h, --help   show this help message and exit

    commands:
      {hello,sum}  available commands
        hello      Say hello to people
        sum        Sum all the given numbers

    $ python nargs.py hello -h
    usage: nargs.py hello [-h] [-names [NAMES [NAMES ...]]]

    optional arguments:
      -h, --help            show this help message and exit
      -names [NAMES [NAMES ...]]

    $ python nargs.py hello
    Hello, Mary!
    Hello, John!

    $ python nargs.py hello -names Alice Bob Alex
    Hello, Alice!
    Hello, Bob!
    Hello, Alex!

    $ python nargs.py sum -h
    usage: nargs.py sum [-h] numbers [numbers ...]

    positional arguments:
      numbers

    optional arguments:
      -h, --help  show this help message and exit

    $ python nargs.py sum 1 2 3 4 5 6
    The sum is 21