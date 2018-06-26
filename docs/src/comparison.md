# Cliar vs. Click vs. docopt

It may seem strange to develop yet another Python package for CLI creation when we already have great tools like Click and docopt. Why not use one of those?

It turns out there's at least one area where Click and docopt just won't do—*modular CLI*. Below, I'll try to explain what I mean by modular CLIs and why they are important. A will also cover other things that make Cliar special.

Name | Modular CLIs | DSL-free | Magic-free | Type casting | Uses type hints
---- | ------------ | -------- | ---------- | ------------ | ---------------
[Cliar](https://moigagoo.github.io/cliar/) | ✔ | ✔ | ✔ | ✔ | ✔
[Click](http://click.pocoo.org/) | ❌ | ✔ | ❌ | ✔ | ❌
[docopt](http://docopt.org/) | ❌ | ❌ | ✔ | ❌ | ❌


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

With docopt, this is simply impossible since CLIs are declared using a DSL:

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

With Click, you can reuse commands from one CLI in another one:

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

However, you can't reuse commands from multiple third-party modules in one CLI this way. That's because command reuse is described with decorators, which leave close to function declarations, not to their call sites: you can't decorate an imported function. In other words, you can create a new player that implements `seek` and borrows `play` from `player`, but you can't add `seek` into `player`.
