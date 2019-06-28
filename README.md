[![image](https://img.shields.io/pypi/v/cliar.svg)](https://pypi.org/project/cliar)
[![image](https://travis-ci.org/moigagoo/cliar.svg?branch=develop)](https://travis-ci.org/moigagoo/cliar)
[![image](https://codecov.io/gh/moigagoo/cliar/branch/develop/graph/badge.svg)](https://codecov.io/gh/moigagoo/cliar)

# Cliar

**Cliar** is a Python package to help you create commandline interfaces. It focuses on simplicity and extensibility:

-   Creating a CLI is as simple as subclassing from `cliar.Cliar`.
-   Extending a CLI is as simple as subclassing from a `cliar.Cliar` subclass.

Cliar's mission is to let you focus on the business logic instead of building an interface for it. At the same time, Cliar doesn't want to stand in your way, so it provides the means to customize the generated CLI.


## Installation

```shell
$ pip install cliar
```

Cliar requires Python 3.6+ and is tested on Windows, Linux, and macOS. There are no dependencies outside Python's standard library.


## Basic Usage

Let's create a commandline calculator that adds two floats:

```python
from cliar import Cliar


class Calculator(Cliar):
'''Calculator app.'''

    def add(self, x: float, y: float):
    '''Add two numbers.'''

        print(f'The sum of {x} and {y} is {x+y}.')


if __name__ == '__main__':
    Calculator().parse()
```

Save this code to `calc.py` and run it. Try different inputs:

-   Valid input:

        $ python calc.py add 12 34
        The sum of 12.0 and 34.0 is 46.0.

-   Invalid input:

        $ python calc.py add foo bar
        usage: calc.py add [-h] x y
        calc.py add: error: argument x: invalid float value: 'foo'

-   Help:

        $ python calc.py -h
        usage: calc.py [-h] {add} ...

        Calculator app.

        optional arguments:
        -h, --help  show this help message and exit

        commands:
        {add}       Available commands:
            add       Add two numbers.

-   Help for `add` command:

        $ python calc.py add -h
        usage: calc.py add [-h] x y

        Add two numbers.

        positional arguments:
        x
        y

        optional arguments:
        -h, --help  show this help message and exit

A few thing to note:

-   It's a regular Python class with a regular Python method. You don't need to learn any new syntax to use Cliar.

-   `add` method is converted to `add` command, its positional params are converted to positional commandline args.

-   There is no explicit conversion to float for `x` or `y` or error handling in the `add` method body. Instead, `x` and `y` are just treated as floats. Cliar converts the types using `add`'s type hints. Invalid input doesn't even reach your code.

-   The `--help` and `-h` flags are added automatically and the help messages are generated from the docstrings.


## Read Next

-   [Tutorial →](https://moigagoo.github.io/cliar/tutorial/)
-   [Cliar vs. Click vs. docopt →](https://moigagoo.github.io/cliar/comparison/)
