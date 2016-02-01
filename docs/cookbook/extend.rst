*************
Extending CLI
*************

:download:`Download source <extend.py>`

.. literalinclude:: extend.py

Usage:

.. code-block:: bash

    $ python extend.py -h
    usage: extend.py [-h] {restart,start,stop} ...

    Extended CLI that overrides one basic command and add one new one.

    optional arguments:
      -h, --help            show this help message and exit

    commands:
      {restart,start,stop}  available commands
        restart             Restart a server = stop + start
        start               Start a server with additional stuff before and after.
        stop                Stop a server

    $ python extend.py start -h
    usage: extend.py start [-h] server

    positional arguments:
      server

    optional arguments:
      -h, --help  show this help message and exit

    $ python extend.py start google.com
    >> Do stuff before server start
    > Starting google.com
    >> Do stuff after server start

    $ python extend.py stop google.com
    > Stopping google.com

    $ python extend.py restart google.com
    >> Restarting google.com:
    > Stopping google.com
    >> Do stuff before server start
    > Starting google.com
    >> Do stuff after server start