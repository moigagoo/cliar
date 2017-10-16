*****
Cliar
*****

Create CLIs from Python classes. Make them powerful with type hints.

.. image:: https://img.shields.io/pypi/v/cliar.svg?style=flat-squar
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/cliar.svg?style=flat-square
    :alt: Downloads

.. image:: https://img.shields.io/pypi/l/cliar.svg?style=flat-square
    :alt: License


.. toctree::
    :hidden:

    cookbook/index
    api


**Cliar** is a Python tool that helps you create commandline interfaces:

.. code-block:: python

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

Cliar runs with Python 3.5+ on Windows, Linux, and Mac. There are no external dependencies.


Install
=======

Install Cliar from `PyPI <https://pypi.python.org/pypi/cliar>`__ with pip:

.. code-block:: bash

    $ pip install cliar

You can install Cliar on CentOS 6 with yum from `Gleb Goncharov's public repo <https://github.com/gongled/gongled-repo>`__:

.. code-block:: bash

    $ yum install -y python-cliar


Hello World
===========

.. code-block:: python

    from cliar import CLI


    class Hello(CLI):
        def hello(self, name='world'):
            print('Hello ' + name + '!')

    if __name__ == '__main__':
        Hello().parse()

.. code-block:: bash

    python hello.py hello --name Bob
    Hello Bob!


Contribute
==========

`Report a bug <https://bitbucket.org/moigagoo/cliar/issues/new>`__

`Fork and improve <https://bitbucket.org/moigagoo/cliar/fork>`__
