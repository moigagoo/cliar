.. image:: https://img.shields.io/pypi/v/cliar.svg
  :target: https://pypi.org/project/cliar
.. image:: https://codecov.io/gh/moigagoo/cliar/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/moigagoo/cliar

*****
Cliar
*****

Create a CLI from a Python class, make it powerful with type hints.

**Cliar** is a Python tool that helps you create commandline interfaces:

.. code-block:: python

    from cliar import Cliar

    class Git(Cliar):
        '''Git clone created with Cliar'''

        def clone(self, repo, dir='.'):
            '''Clone a git repo from REPO to DIR.'''

            print(f'Cloning from {repo} to {dir}')

    if __name__ == '__main__':
        Git().parse()

Run the script:

.. code-block:: bash

    $ python git.py clone http://foo.bar -d baz
    Cloning from http://foo.bar to baz


Requirements
============

Cliar runs with Python 3.6+ on Windows, Linux, and Mac. There are no external dependencies.


Install
=======

Install Cliar from `PyPI <https://pypi.org/project/cliar>`__ with pip:

.. code-block:: bash

    $ pip install cliar
