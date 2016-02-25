**************************
Cliar: Create CLIs Clearly
**************************

.. image:: https://img.shields.io/pypi/v/cliar.svg?style=flat-squar
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/cliar.svg?style=flat-square
    :alt: Downloads

.. image:: https://img.shields.io/pypi/l/cliar.svg?style=flat-square
    :alt: License


.. toctree::
    :hidden:

    cookbook/index
    python2
    api


**Cliar** (pronounced as "clear") is a Python tool that helps you create command-line interfaces::

    from cliar import CLI

    class Git(CLI):
        '''Git clone created with Cliar'''

        def clone(self, repo, dir='.'):
            '''Clone a git repo from REPO to DIR.'''

            print('Cloning from %s to %s' % (repo, dir))

    if __name__ == '__main__':
        Git().parse()

Run the script:

.. code-block:: bash

    $ python git.py clone http://foo.bar -d baz
    Cloning from http://foo.bar to baz


Requirements
============

Cliar runs with Python 2.6, 2.7, and 3.3+ on Windows, Linux, and Mac. There are no dependencies.


Install
=======

Install Cliar from `PyPI <https://pypi.python.org/pypi/cliar>`__ with pip:

.. code-block:: bash

    $ pip install cliar

You can install Cliar on CentOS 6 with yum from `Gleb Goncharov's public repo <https://github.com/gongled/gongled-repo>`__:

.. code-block:: bash

    $ yum install -y python-cliar


Why another CLI tool?
=====================

There're two major CLI tools for Python: `docopt <http://docopt.org/>`_ and `click <http://click.pocoo.org/5/>`_. Before creating Cliar, I tried them both.

Neither click, not docopt allow for easily extensible CLIs. Cliar lets you extend your CLI with plain subclassing.


Limitations
===========

Cliar is designed to help you create CLIs quickly. For the sake of simplicity, some features are not available:

    -   You can't add help text for arguments. You can add help text for commands via docstrings.
    -   Optional arguments are given in the form "-name, " not "--name." This is unconvential yet totally valid.
    -   You can't have 3rd-level commands.
    -   Cliar can't do a lot of things argparse can, but the idea is that you probably don't need most of them.


Contribute
==========

`Report a bug <https://bitbucket.org/moigagoo/cliar/issues/new>`__

`Fork and improve <https://bitbucket.org/moigagoo/cliar/fork>`__
