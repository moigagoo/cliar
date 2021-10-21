# Tutorial

This quick tutorial will guide you through all Cliar's features. We'll start with a simple "Hello World" example and progressively add features to it.

>   Download the complete app: [greeter.py](assets/greeter.py)


## Hello World

Here's the simplest "Hello World" program with Cliar:

```python
from cliar import Cliar

class Greeter(Cliar):
    def hello(self):
        print('Hello World!')

if __name__ == '__main__':
    Greeter().parse()
```

In Cliar, CLI is a subclass of `Cliar`, with its methods turned into commands and their params into args.

Save this code into `greeter.py` and run it:

```shell
$ python greeter.py hello
Hello World!
```


## Optional Flags

Let's add a `--shout` flag to `hello`:

```python
    def hello(self, shout=False):
        greeting = 'Hello World!'
        print(greeting.upper() if shout else greeting)

```

Try running `greeter.py` with and without the newly defined flag:

```shell
$ python greeter.py hello --shout
HELLO WORLD!

$ python greeter.py hello -s
HELLO WORLD!

$ python greeter.py hello
Hello World!
```


## Positional Arguments

Positional args are added the same way as flags.

```python
    def hello(self, name, shout=False):
        greeting = f'Hello {name}!'
        print(greeting.upper() if shout else greeting)
```

Try it:

```shell
$ python greeter.py hello John
Hello John!

$ python greeter.py hello John --shout
HELLO JOHN!

$ python greeter.py hello -s John
HELLO JOHN!

$ python greeter.py hello
usage: greeter.py hello [-h] [-s] name
greeter.py hello: error: the following arguments are required: name
```


## Help Messages

Cliar automatically registers `--help` flag for the program itself and its every command:

```shell
$ python greeter.py --help
usage: greeter.py [-h] {hello} ...

optional arguments:
  -h, --help  show this help message and exit

commands:
  {hello}     Available commands:
    hello

$ python greeter.py hello --help
usage: greeter.py hello [-h] [-s] name

positional arguments:
  name

optional arguments:
  -h, --help   show this help message and exit
  -s, --shout
```

Command help messages are generated from docstrings. Let's add them:

```python
class Greeter(Cliar):
    '''Greeter app created with Cliar.'''

    def hello(self, name, shout=False):
        '''Say hello.'''

        greeting = f'Hello {name}!'
        print(greeting.upper() if shout else greeting)
```

and view the updated help message:

```shell
$ python greeter.py -h
usage: greeter.py [-h] {hello} ...

Greeter app created with Cliar.

optional arguments:
  -h, --help  show this help message and exit

commands:
  {hello}     Available commands:
    hello     Say hello.

$ python greeter.py hello -h
usage: greeter.py hello [-h] [-s] name

Say hello.

positional arguments:
  name

optional arguments:
  -h, --help   show this help message and exit
  -s, --shout
```

To add description for arguments, use `set_help` decorator:

```python
from cliar import Cliar, set_help

...

    @set_help({'name': 'Who to greet', 'shout': 'Shout the greeting'})
    def hello(self, name, shout=False):
        '''Say hello.'''

        greeting = f'Hello {name}!'
        print(greeting.upper() if shout else greeting)
```

The decorator takes a mapping from param names to help messages.

Call the help message for `hello` command:

```shell
$ python greeter.py hello -h
usage: greeter.py hello [-h] [-s] name

Say hello.

positional arguments:
  name         Who to greet

optional arguments:
  -h, --help   show this help message and exit
  -s, --shout  Shout the greeting
```

To show default values for flags, add `show_defaults = True` to `set_help`:

```python
...
    @set_help(
        {'name': 'Who to greet', 'shout': 'Shout the greeting'},
        show_defaults = True
    )
    def hello(self, name, shout=False):
...
```

Call help again to see the default value:

```shell
$ python greeter.py hello -h
usage: greeter.py hello [-h] [-s] name

Say hello.

positional arguments:
  name         Who to greet

optional arguments:
  -h, --help   show this help message and exit
  -s, --shout  Shout the greeting (default: False)
```


## Metavars

*Metavar* is a placeholder of a positional arg as it appears in the help message. By default, Cliar uses the param name as its metavar. So, for `name` param the metavar is called `name`:

```shell
$ python greeter.py hello -h
usage: greeter.py hello [-h] [-s] name

Say hello.

positional arguments:
  name         Who to greet

optional arguments:
  -h, --help   show this help message and exit
  -s, --shout  Set to shout the greeting
```

To set a different metavar for a param, usd `set_metavars` decorator:

```python
from cliar import Cliar, set_help, set_metavars

...

    @set_metavars({'name': 'NAME'})
    @set_help({'name': 'Who to greet', 'shout': 'Shout the greeting'})
    def hello(self, name, shout=False):
        '''Say hello.'''

        greeting = f'Hello {name}!'
        print(greeting.upper() if shout else greeting)
```

The decorator takes a mapping from param names to metavars.

Call the help message for `hello`:

```shell
usage: greeter.py hello [-h] [-s] NAME

Say hello.

positional arguments:
  NAME         Who to greet

optional arguments:
  -h, --help   show this help message and exit
  -s, --shout  Set to shout the greeting
```


## Type Casting

Cliar casts arg types of args on the fly. To use type casting, add type hints or default values to params.

Let's add `-n` flag that will tell how many times to repeat the greeting:

```python
    @set_metavars({'name': 'NAME'})
    @set_help({'name': 'Who to greet', 'shout': 'Shout the greeting'})
    def hello(self, name, n=1, shout=False):
        '''Say hello.'''

        greeting = f'Hello {name}!'

        for _ in range(n):
            print(greeting.upper() if shout else greeting)
```

Let's call `hello` with the new flag:

```shell
$ python greeter.py hello John -n 2
Hello John!
Hello John!
```

If we pass a non-integer value to `-n`, an error occurs:

```shell
$ python greeter.py hello John -n foo
usage: greeter.py hello [-h] [-n N] [-s] NAME
greeter.py hello: error: argument -n/--n: invalid int value: 'foo'
```

!!! hint

    You can use any callable as a param type, and it will be called to cast the param type during parsing. One useful example is using `open` as the param type:

        def read_from_file(input_file: open):
            lines = input_file.readlines()

    If you pass a path to such a param, Cliar will open it and pass the resulting file-like object to the handler body. And when the handler returns, Cliar will make sure the file gets closed.


## Argument Names

By default, Cliar takes the param name, replaces underscores with dashes, and uses that as the corresponding arg name: `name` is turned into `--name`, and `upper_limit` into `--upper-limit`; the first letter is used as a short option: `-n` for `--name`, `-u` for `--upper-limit`.

To use different arg names, use `set_arg_map` decorator:

```python
from cliar import Cliar, set_help, set_metavars, set_arg_map

...

    @set_arg_map({'n': 'repeat'})
    @set_metavars({'name': 'NAME'})
    @set_help({'name': 'Who to greet', 'shout': 'Shout the greeting'})
    def hello(self, name, n=1, shout=False):
        '''Say hello.'''

        greeting = f'Hello {name}!'

        for _ in range(n):
            print(greeting.upper() if shout else greeting)
```

Now use `--repeat` or `-r` instead of `-n`:

```shell
$ python greeter.py hello John --repeat 2
Hello John!
Hello John!

$ python greeter.py hello John -r 2
Hello John!
Hello John!
```

!!! hint

    This decorator lets you use Python's reserved words like `--for` and `--with` as arg names.

You can also override argument short names specifically, with `set_sharg_map` decorator:

```python
from cliar import Cliar, set_help, set_metavars, set_arg_map, set_sharg_map

...

    @set_arg_map({'n': 'repeat'})
    @set_sharg_map({'n': 'n'})
    @set_metavars({'name': 'NAME'})
    @set_help({'name': 'Who to greet', 'shout': 'Shout the greeting'})

    def hello(self, name, n=1, shout=False):
        '''Say hello.'''

        greeting = f'Hello {name}!'

        for _ in range(n):
            print(greeting.upper() if shout else greeting)
```

Now you can use `-n` instead of `-r`:

```shell
$ python greeter.py hello John --repeat 2
Hello John!
Hello John!

$ python greeter.py hello John -n 2
Hello John!
Hello John!
```

This is useful when you have several arguments that start with the same letter, which creates a conflict between short arg names.

To disable short argument variant entirely, set the short arg name to `None`: ```@set_sharg_map({'argname': None})```.


## Multiple Commands

Adding more commands to the CLI simply means adding more methods to the CLI class:

```python
class Greeter(Cliar):
    def goodbye(self, name):
        '''Say goodbye'''

        print(f'Goodbye {name}!')

    @set_arg_map({'n': 'repeat'})
    ...
```

With this code addition, you can call `goodbye` command:

```shell
$ python greeter.py goodbye Mary
Goodbye Mary!
```


## Nested Commands

You can have any level of nested commands by adding Cliar CLIs as class attributes.

For example, let's add a `utils` subcommand with its own `time` subcommand that has `now` command:

```python
class Time(Cliar):
    def now(self, utc=False):
        now_ctime = datetime.utcnow().ctime() if utc else datetime.now().ctime()
        print(f'UTC time is {now_ctime}')

class Utils(Cliar):
    time = Time

class Greeter(Cliar):
    '''Greeter app created with in Cliar.'''

    utils = Utils

    def _root(self, version=False):
        ...
```

You can now call `now` command through `utils`:

```shell
$ python greeter.py utils time now
Local time is Sun Jul 21 15:25:52 2019

$ python greeter.py utils time now --utc
UTC time is Sun Jul 21 11:25:57 2019
```


## Command Aliases

To add aliases to a command, use `add_aliases` decorator:

```python
from cliar import Cliar, set_help, set_metavars, set_arg_map, add_aliases

...

    @add_aliases(['mientras', 'пока'])
    def goodbye(self, name):
        '''Say goodbye'''

        print(f'Goodbye {name}!')
```

Now you can call `goodbye` command by its aliases:

```shell
$ python greeter.py mientras Maria
Goodbye Maria!

$ python greeter.py пока Маша
Goodbye Маша!
```


## Command Names

By default, CLI commands are named after the corresponding methods. To override this behavior and set a custom command name, use `set_name` decorator:

```python
from cliar import Cliar, set_help, set_metavars, set_arg_map, add_aliases, set_name


class Greeter(Cliar):
    '''Greeter app created with in Cliar.'''

    @set_name('factorial')                  # Name the command `factorial`
    def calculate_factorial(self, n: int):  # because `calculate_factorial`
        '''Calculate factorial'''           # is too long for CLI.

        print(f'n! = {factorial(n)}')
```

Now `calculate_factorial` is called with `factorial` command:

```shell
$ python greeter.py factorial 4
n! = 24

$ python greeter.py calculate_factorial 4
usage: greeter.py [-h] {factorial,goodbye,mientras,пока,hello} ...
greeter.py: error: argument command: invalid choice: 'calculate_factorial' (choose from 'factorial', 'goodbye', 'mientras', 'пока', 'hello')
```


## Ignore Methods

By default, Cliar converts all non-static and non-class methods of the `Cliar` subclass into CLI commands.

There are two ways to tell Cliar *not* to convert a method into a command: start its name with an underscore or use `ignore` decorator:

```python
from math import factorial, tau, pi

from cliar import Cliar, set_help, set_metavars, set_arg_map, add_aliases, set_name, ignore


class Greeter(Cliar):
    '''Greeter app created with in Cliar.'''

    def _get_tau_value(self):
        return tau

    @ignore
    def get_pi_value(self):
        return pi

    def constants(self):
        print(f'τ = {self._get_tau_value()}')
        print(f'π = {self.get_pi_value()}')

    ...
```

Only `constants` method will be exposed as a CLI command:

```shell
$ python greeter.py constants
τ = 6.283185307179586
π = 3.141592653589793

$ python greeter.py get-pi-value
usage: greeter.py [-h] {factorial,constants,goodbye,mientras,пока,hello} ...
greeter.py: error: argument command: invalid choice: 'get-pi-value' (choose from 'factorial', 'constants', 'goodbye', 'mientras', 'пока', 'hello')
```


## Root Command

To assign action to the root command, i.e. the script itself, define `_root` method:

```python
class Greeter(Cliar):
    '''Greeter app created with in Cliar.'''

    def _root(self, version=False):
        print('Greeter 1.0.0.' if version else 'Welcome to Greeter!')
    ...
```

If you run `greeter.py` with `--version` or `-v` flag, you'll see its version. If you call `greeter.py` without any flags or commands, you'll see a welcome message:

```shell
$ python greeter.py
Welcome to Greeter!

$ python greeter.py --version
Greeter 1.0.0.
```


## Global Arguments

Global arguments defined in `_root` can be accessed in commands via `self.global_args`:

```python
    ...

    def constants(self):
        if self.global_args.get('version'):
            print('Greeter 1.0.0.')

        print(f'τ = {self._get_tau_value()}')
        print(f'π = {self.get_pi_value()}')

    ...
```

Run `constants` with `--version`:

```shell
$ python greeter.py --version constants
Greeter 1.0.0.
τ = 6.283185307179586
π = 3.141592653589793
```

This works with [nested commands](#nested-commands), too. Global arguments of nested commands override global arguments of their parents.
