[![image](https://img.shields.io/pypi/v/cliar.svg)](https://pypi.org/project/cliar)
[![image](https://travis-ci.org/moigagoo/cliar.svg?branch=develop)](https://travis-ci.org/moigagoo/cliar)
[![image](https://codecov.io/gh/moigagoo/cliar/branch/develop/graph/badge.svg)](https://codecov.io/gh/moigagoo/cliar)

# Cliar

**Cliar** is a Python tool that helps you create commandline interfaces:

```python
from cliar import Cliar

class Git(Cliar):
    '''Git clone created with Cliar'''

    def clone(self, repo, dir='.'):
        '''Clone a git repo from REPO to DIR.'''

        print(f'Cloning from {repo} to {dir}')

if __name__ == '__main__':
    Git().parse()
```

Run the script:

```bash
$ python git.py clone http://foo.bar -d baz
Cloning from http://foo.bar to baz
```

## Requirements

Cliar runs with Python 3.6+ on Windows, Linux, and Mac. There are no external dependencies.

## Install

Install Cliar from PyPI with pip:

```bash
$ pip install cliar
```
