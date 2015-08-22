**************************************
Cliar: Create CLIs Quickly and Clearly
**************************************

.. image:: https://img.shields.io/pypi/v/cliar.svg?style=flat-squar 
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/cliar.svg?style=flat-square
    :alt: Downloads

.. image:: https://img.shields.io/pypi/l/cliar.svg?style=flat-square
    :alt: License

Cliar (read as "clear") is a thin wrapper around argparse that lets you create extendable command-line interfaces in a quick and clear way:

    Your CLI is a subclass of ``cliar.CLI``, and your CLI commands are its methods. Command-line args are generated based on method params.


Requirements
============

Cliar runs with Python 3.3+ on Windows, Linux, and Mac with not third party dependencies.


Install
=======

Install Sloth from `PyPI <https://pypi.python.org/pypi/cliar>`__ with pip:

.. code-block:: bash

    $ pip install cliar


Quickstart
==========

Creating a CLI with Cliar is as simple as::

    from cliar import CLI

    class MyCLI(CLI):
        '''This is my own command-line interface built with Cliar'''
        
        def start(self, awesome=False):
            '''This is a command in my CLI. Apparently, it starts something.'''

            print('Started...')

            if awesome:
                print("...and it's awesome!")

            else:
                print('...with no awesomeness.')

    if __name__ == '__main__':
        MyCLI()

That's it. Save to a file and run:

.. code-block:: bash

    $ python mycli.py start
    Started...
    ...with no awesomeness.

    $ python mycli.py start -a #or -awesome, or -awe
    Started...
    ...and it's awesome!

The ``start`` method created the ``start`` CLI command. The ``awesome`` param created the ``awesome`` argument for the ``start`` command. Because the ``awesome`` param has a default value, the CLI argument is not required, i.e. is prefixed with a dash. Remove the default value to get a positional required argument.

Cliar knows that if a method expects a boolean, the corresponding command-line argument must be a flag.

You can name the CLI command differently than its corresponding method with the ``cliar.set_name`` decorator::

    from cliar import set_name

    #...

        @set_name('launch')
        def start(self, awesome=False):

        # ...

Now, the ``launch`` command calls the ``start`` method:

.. code-block:: bash

    $ python mycli.py launch
    Started...
    ...with no awesomeness.

Let's add another command::

    # ...

    def say(self, word:str, n:int=1):
        '''This command says stuff.'''

        for _ in range(n):
            print(word)

    # ...

See it in action:

.. code-block:: bash

    $ python mycli.py say Hi!
    Hi!

    $ python mycli.py say Hi! -n 3
    Hi!
    Hi!
    Hi!

Cliar uses annotations and default values to validate arguments.

Now let's add a global argument::

    # ...

    def _root(self, capitalize=False):
        self.capitalize = capitalize
        
        if capitalize:
            print('Everything you say will be in CAPS.')

    def say(self, word:str, n:int=1):
        #...
        
        if self.capitalize:
            word = word.upper()
        
        #...

Use it:

.. code-block:: bash

    $ python mycli.py -c say hello #or -capitalize, or -cap
    HELLO

The special ``_root`` method corresponds to the root command, i.e. the script itself. It's always executed before any other command methods.

Finally, let's extend our CLI. Save this code as myextendedcli.py::

    from mycli import MyCLI

    class MyExtendedCLI(MyCLI):
        '''This is the extended version of my command-line interface'''

        def goodbye(self):
            print('Good bye, and happy hacking!')

    if __name__ == '__main__':
        MyExtendedCLI()

Run it:

.. code-block:: bash

    $ python myextendedcli.py goodbye
    Good bye, and happy hacking!

    $ python myextendedcli.py -c say "Hello, extension"
    HELLO, EXTENSION

    $ python myextendedcli.py -h
    usage: myextendedcli.py [-h] [-capitalize] {goodbye,start,say} ...

    This is the extended version of my command-line interface

    optional arguments:
      -h, --help           show this help message and exit
      -capitalize

    commands:
      {goodbye,start,say}  available commands
        goodbye
        start              This is a command in my CLI. Apparently, it starts
                           something.
        say                This command says stuff.


Why another CLI tool?
=====================

I know there're great projects like `docopt <http://docopt.org/>`_ and `click <http://click.pocoo.org/5/>`_ out there. Before creating Cliar, I tried them both.

Long story sort, **neither click, not docopt allow for easily extendible CLIs. On the other hand, Cliar lets you extend your CLI with simple subclassing.**

By extendability I mean the ability to extend CLI described in one module with commands from another module.

In docopt, this would mean overriding the entire help string or inserting a line into it, which is neither elegant, nor flexible, nor stable.

In click, commands are just functions in the global namespace, and nesting is done with the ``group`` decorator. Extending can be done with importing * from one module to another, which is bad practice. Putting the commands inside a class doesn't work as expected, which makes it impossible to extend CLI with subclassing.


Limitations
===========

Cliar is designed to help you create CLIs quickly and with as little code as possible. For the sake of simplicity, some features are not available:

    -   You can't add help text for arguments. You can though add help text for commands via docstrings.
    -   Optional arguments are given in the form "-name, " which is unconvential, however valid. You can abbreviate optional arguments until it's unambiguous.
    -   No third level commands.
    -   Generally speaking, Cliar can't do a lot of things argparse can, but the idea is that you probably don't need most of these things.


Contribute
==========

`Report a bug <https://bitbucket.org/moigagoo/cliar/issues/new>`__

`Fork and improve <https://bitbucket.org/moigagoo/cliar/fork>`__
