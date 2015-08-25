**************************************
Cliar: Create CLIs Quickly and Clearly
**************************************

.. image:: https://img.shields.io/pypi/v/cliar.svg?style=flat-squar 
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/cliar.svg?style=flat-square
    :alt: Downloads

.. image:: https://img.shields.io/pypi/l/cliar.svg?style=flat-square
    :alt: License

Cliar (pronounced as "clear") helps you create command-line interfaces quickly and with minimum code:

.. code-block:: python
    :caption: git.py

    from cliar import CLI

    class Git(CLI):
        '''Git clone created with Cliar'''

        def clone(self, repo, dir='.'):
            '''Clone a git repo from REPO to DIR.'''

            print('Cloning from %s to %s' % (repo, dir))


    if __name__ == '__main__':
        Git()

Run the script:

.. code-block:: bash

    $ python git.py clone http://foo.bar -d baz
    Cloning from http://foo.bar to baz


Requirements
============

Cliar runs with Python 3.3+ on Windows, Linux, and Mac with not third party dependencies.


Install
=======

Install Sloth from `PyPI <https://pypi.python.org/pypi/cliar>`__ with pip:

.. code-block:: bash

    $ pip install cliar


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
