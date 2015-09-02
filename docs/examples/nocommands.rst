***********
No Commands
***********

:download:`Download source <nocommands.py>`

.. literalinclude:: nocommands.py

Usage:

.. code-block:: bash

    $ python nocommands.py -h
    usage: nocommands.py [-h] [-capitalize] {} ...

    This is a CLI without commands; the script itself is a command. Calling the
    script will print this important message. Add "-c" for more dramatism.

    optional arguments:
      -h, --help   show this help message and exit
      -capitalize

    commands:
      {}           available commands

    $ python nocommands.py
    The script itself is a command

    $ python nocommands.py -capitalize
    THE SCRIPT ITSELF IS A COMMAND

    $ python nocommands.py -cap
    THE SCRIPT ITSELF IS A COMMAND

    $ python nocommands.py -c
    THE SCRIPT ITSELF IS A COMMAND
