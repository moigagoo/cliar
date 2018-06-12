# Tutorial

## Greeter App

In Cliar, commandline interface, or CLI, is represented with a Python class subclassed from `cliar.Cliar`. Cliar turns the class methods into commands and their params into args.

Let's create the simplest CLI that says "Hello World!" when you call "hello" command:

```python
from cliar import Cliar


class Greeter(Cliar):           # Define a regular Python class
    def hello(self):            # and a regular method,
        print('Hello World!')   # which implements the business logic.


if __name__ == '__main__':
    greeter = Greeter()         # Create an instance of the class
    greeter.parse()             # and run its `parse` method.
```

Save this code into `greeter.py` and run it with Python:

    $ python greeter.py hello
    Hello World!

And here it is: your first CLI created with Cliar! That was easy, wasn't it?

Let's extend `hello` method to shout the greeting if `--shout` flag is passed:

```python
    def hello(self, shout=False):
        greeting = 'Hello World!'

        if shout:
            print(greeting.upper())
        else:
            print(greeting)
```

Try running `greeter.py` with and without the newly defined flag:

    $ python greeter.py hello --shout
    HELLO WORLD!
    $ python greeter.py hello -s    # Short version works, too!
    HELLO WORLD!
    $ python greeter.py hello
    Hello World!

Cliar did a few things for us here:

-   `shout` is an optional param, so it was converted into an optional flag
-   since `shout` default value is `False`, Cliar inferred its type as `bool`, so we can use it as such inside `hello` body
-   not only was `--shout` flag generated from the eponymous `shout` param, but a short version `-s` was also generated

Ok, but what if we want our app to be able to greet anyone, not just the world? Just add a positional param to `hello`:

```python
    def hello(self, name, shout=False):
        greeting = f'Hello {name}!'

        if shout:
            print(greeting.upper())
        else:
            print(greeting)
```

Try it:

    $ python greeter.py hello John
    Hello John!
    $ python greeter.py hello John --shout
    HELLO JOHN!
    $ python greeter.py hello -s John
    HELLO JOHN!
