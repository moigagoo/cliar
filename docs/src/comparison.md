# Cliar vs. Click vs. docopt

It may seem strange to develop yet another Python package for CLI creation when we already have great tools like Click and docopt. Why not use one of those?

It turns out there's at least one area where Click and docopt just won't do—*modular CLI*. Below, I'll try to explain what I mean by modular CLIs and why they are important. A will also cover other things that make Cliar special.

Name | Modular CLIs | DSL-free | Magic-free | Type casting | Pun in name
---- | ------------ | -------- | ---------- | ------------ | -----------
[Cliar](https://moigagoo.github.io/cliar/) | ✔ | ✔ | ✔ | ✔ | ✔
[Click](http://click.pocoo.org/) | ❌ | ✔ | ❌ | ✔ | ✔
[docopt](http://docopt.org/) | ❌ | ❌ | ✔ | ❌ | ❌

!!! note
    Of course, any tool lets you do anything. When I say "feature X is not supported by tool Y," I mean that the effort needed to implement X with Y is *in my opinion* too high.

    Conclusions are based on official docs of the tools being compared.

    Feel free to disagree.


## Modular CLIs

Imagine you're developing a CLI-based audio player. You want it to have a ton of features but you don't want to develop them all on your own. The core version will only play a given file, but the rest of the functionality will be implemented with extensions.

You want the usage of the player to be something like this:

```shell
$ player play file.mp3          # Core functionality
$ pip install player.ext.seek   # Install extension
$ player seek "1:23"            # Extension-provided functionality
```

This approach has several benefits:

-   the user will be able to install only the parts they need
-   you will be able to delegate responsibility to the community
-   new commands are added via a unified API, which is the same for core and third-party developers

So, your job is provide a way for third parties to add commands to the basic CLI and override existing commands.

**With docopt** this is almost impossible since CLIs are declared in plaintext using a DSL:

```python
'''Player.

Usage:
  player play <file>
  player (-h | --help)

Options:
  -h --help     Show this screen.
'''
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__)
```

Adding a new command means adding a line into a spec before it gets parsed, so the on;y way an extension can add a new command to the base CLI is by inserting lines into the base CLI spec. This is inconvenient if you're adding one command, but it's a nightmare if you're creating an API for adding unlimited commands:

```python
'''Player.

Usage:
  player play <file>
  player (-h | --help)

Options:
  -h --help     Show this screen.
'''
from docopt import docopt

from player.ext.seek import insert_seek_command
# "insert_seek_command" function inserts "player seek <pos>"
# after "player play". You can already feel how quickly it gets old.
if __name__ == '__main__':
    extended_doc = insert_seek_command(__doc__)
    arguments = docopt(extended_doc)
```

**With Click**, you can reuse commands from one CLI in another one:

```python
# In file a:
cli = click.Group()

@cli.command()
def cmd_a(): print("You called cmd_a")


# In file b:

from a import cli

@cli.command()
def cmd_b(): print("You called cmd_b")
```

>  Thanks to /u/Brian for the [code sample](https://www.reddit.com/r/Python/comments/3j28oa/cliar_create_clis_clearly_cliar_103_documentation/culnqg2).

However, you can't reuse commands from multiple third-party modules in one CLI, which is what we want. That's because command reuse relations are defined with decorators, and you can't decorate an imported function. In other words, you can create a new player that implements `seek` and borrows `play` from `player`, but you can't add `seek` into `player`.

**With Cliar**, extending an existing CLI is trivial. Since in Cliar a CLI is a regular Python class, extending it means extending the class the most natural way—with inheritance. Just subclass your CLI from as many ``Cliar`` ancestors as you need:

```python
from cliar import Cliar

# Basic CLI:
class BasicCLI(CLiar):
    def play(self, path):
        ...

# Seek extension:
class SeekCLI(Cliar):
    def seek(self, position):
        ...

# Complete CLI:

class CLI(BasicCLI, SeekCLI, *MoreExtensions):
    '''The complete CLI that borrows from the basic CLI and extensionss.

    Notice that the class body is empty: the logic is already implemented by the parents.
    '''
    pass
```

Cliar relies on Python's standard mechanisms and doesn't reinvent the wheel when it comes to adding new features to objects. Python supports both single and multiple inheritance, so CLI extension goes both ways: you can create a completely new interface that borrows from an existing one or build an interface from extensions.


## DSL-Free

DSLs should be avoided when pure Python is enough. A DSL requires time to learn, and the knowledge you gain is useless outside the scope of the DSL, which is by definition the app it's used in.

!!! note

    This thought has been explained by Robert E Brewer in [The Zen in CherryPy](https://pyvideo.org/pycon-us-2010/pycon-2010--the-zen-of-cherrypy---111.html).

**In Docopt**, you describe your CLI using a DSL. Then, you ask docopt to parse the commandline string and pass the extracted values to the business logic. The interface is completely separated from the business logic.

It may seem a good idea until you actually start using docopt. What happens is you end up duplicating argument definitions all the time:

```python
'''Player.

Usage:
  player play <file>
  player seek <position>
  player (-h | --help)

Options:
  -h --help     Show this screen.
'''                                     # one time
from docopt import docopt


def play(file):                         # two times
    ...

def seek(position):
    ...

if __name__ == '__main__':
    arguments = docopt(__doc__)

    if arguments.get('play'):           # three times
        play(arguments['<file>'])
    elif arguments.get('seek'):
        seek(arguments['<position>'])
    ...                                 # ...and it goes on and on and on.
```

Even in this toy example you can see how much redundant code this pattern spawns.

**Click** and **Cliar** are DSL-free. Whereas docopt is "spec first," Click and Cliar are "code first": they generate the usage text from the code, not the other way around.


## Magic-Free

*Magic* is unusual behavior driven by a hidden mechanism. It may give a short "wow" effect, but the price to pay is that code becomes harder to debug and harder to follow. Writing idiomatic Python generally means avoiding magic.

To see if a tool is "magical," remove it from the code and see if the code breaks.

**Docopt**, for example, is magic-free. If you remove the `__doc__` parsing part, the remaining code is still 100% valid Python. Removing docopt does not break you program, it just removes the commandline parsing functionality:

```python
'''Player.

Usage:
  player play <file>
  player (-h | --help)

Options:
  -h --help     Show this screen.
'''
# from docopt import docopt

if __name__ == '__main__':
    # arguments = docopt(__doc__)
    pass
```

**Click**, on the other hand, is full of magic. Let's examine the hello world example from the [Click documentation](http://click.pocoo.org/):

```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
```

Note that `hello` function accepts two positional arguments, `count` and `name`, but we call it without any arguments. That's because the params are added by the decorators based on the arguments of the decorator generators (`--count` and `--name`). This is broken code only forced to work by the magic of Click's decorators.

**Cliar** is magic-free. Your CLI classes are regular Python classes. If you remove `Cliar` from its parents, the class will remain functional. It will continue to contain all the business logic, only without the CLI:

```python
# from cliar import Cliar

# class Player(Cliar):
class Player(object):
    def play(self, file):
        print(f'Playing {file}')
```

Cliar's decorators like `set_name` or `add_aliases` can also be safely remove without breaking any code.


## Type Casting

In commandline, any argument or flag value is a string. Converting strings to numbers and other types manually within business logic is tedious, requires dancing with exception handling, and, most importantly, has nothing to do with the business logic itself: it's a necessity induced by the fact the shell works only with strings and Python works with all sorts of types rather than a valuable data processing within business logic.

**Docopt** doesn't attempt to cast types. It just parses a string into smaller ones in a nicely structured way, leaving all the necessary processing to the programmer:

```python
args = docopt(__doc__)

if args['play']:
    file = Path(args['<file>'])
```

**Click** lets you define an argument and option type in the decorator constructor:

```python
@click.argument('num', type=int)
```

If the type is not set, Click tries to infer it from the default value. It that's not set as well, string is assumed.

**Cliar** lets you define argument and option type with type hints. The logic is similar to Click's: if the type hint is given, use it, if not, infer the type from the default value, otherwise assume string:

```python
def play(file: Path, num=1)
```
