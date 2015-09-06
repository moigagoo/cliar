*********
Git Clone
*********

:download:`Download source <git.py>`

.. literalinclude:: git.py

Usage:

.. code-block:: bash

    $ python git.py -h
    usage: git.py [-h] [-config CONFIG] {clone,checkout} ...

    This is a Git CLI clone. It doesn't actually do stuff, just it imitates 2 git
    commands.

    optional arguments:
      -h, --help        show this help message and exit
      -config CONFIG

    commands:
      {clone,checkout}  available commands
        clone           Clone REPO to DIR
        checkout        Checkout to BRANCH. Use "-f" for force and "-q" for quiet.

    $ python git.py clone -h
    usage: git.py clone [-h] [-dir DIR] repo

    positional arguments:
      repo

    optional arguments:
      -h, --help  show this help message and exit
      -dir DIR

    $ python git.py checkout -h
    usage: git.py checkout [-h] [-force] [-quiet] branch

    positional arguments:
      branch

    optional arguments:
      -h, --help  show this help message and exit
      -force
      -quiet

    $ python git.py clone http://myrepo.com
    Cloning the repo: http://myrepo.com. Destination: .

    $ python git.py clone http://myrepo.com -d ~/myrepo
    Cloning the repo: http://myrepo.com. Destination: ~/myrepo

    $ python git.py checkout dev
    Checking out to dev

    $ python git.py checkout dev -f
    Checking out to dev
    Forced checkout

    $ python git.py checkout dev -q
    Checking out to dev
    Quiet checkout

    $ python git.py -c ~/myconfig checkout dev
    The config is: ~/myconfig
    Checking out to dev