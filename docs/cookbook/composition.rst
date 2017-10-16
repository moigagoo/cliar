***************
CLI Composition
***************

Consider the following scenario. Your have an app that exposes a basic CLI. You also have extensions that should be able to extend and override the basic CLI commands.

In other words, you need a way to construct a CLI from multiple CLIs, possibly coming from different places.

:download:`Download source <composition.py>`

.. literalinclude:: composition.py

Usage:

.. code-block:: bash

    $ python composition.py
    usage: composition.py [-h] {hello,say-a,say-b} ...

    optional arguments:
    -h, --help           show this help message and exit

    commands:
    {hello,say-a,say-b}  Available commands:
        hello
        say-a
        say-b

    $ python composition.py hello -h
    usage: composition.py hello [-h] name

    positional arguments:
    name

    optional arguments:
    -h, --help  show this help message and exit

    $ python composition.py hello Bob
    Hello, Bob!

    $ python composition.py say-a -h
    usage: composition.py say-a [-h] [-n NUMBER]

    optional arguments:
    -h, --help            show this help message and exit
    -n NUMBER, --number NUMBER

    $ python composition.py say-a --number 10
    aaaaaaaaaa
