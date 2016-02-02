*********************
The ``open`` Arg Type
*********************

.. note:: This example works in Python 3 only.

If you set arg type to ``open``, Cliar will attempt to locate and read from the filepath passed to this arg.

In fact, arg type can be any Python callable that accepts a string, including custom functions. `Read more <https://docs.python.org/3/library/argparse.html#type>`__ in the argparse docs.

:download:`Download source <openfile.py>`

.. literalinclude:: openfile.py

Usage:

.. code-block:: bash

    $ python openfile.py -h
    usage: openfile.py [-h] {find_word} ...

    This CLI has a command that takes a filepath and attempts to open it on
    the fly.

    optional arguments:
      -h, --help   show this help message and exit

    commands:
      {find_word}  available commands
        find_word  Find WORD in FILE

    $ python openfile.py find_word -h
    usage: openfile.py find_word [-h] file word

    positional arguments:
      file
      word

    optional arguments:
      -h, --help  show this help message and exit

    $ python openfile.py find_word openfile.rst python
    Here it is!

    $ python openfile.py find_word openfile.rst perl
    Nope, not here

    $ python openfile.py find_word foo bar
    ...
    FileNotFoundError: [Errno 2] No such file or directory: 'foo'