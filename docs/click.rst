***************
Cliar vs. Click
***************

Click
=====

`Click <http://click.pocoo.org/>`_ is a package for building command-line interfaces, created by Armin Ronacher.

Click relies heavily on decorators. Every command is a decorated function, and every option is an additional decorator:

.. code-block:: python

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

Moreover, a group of commands is also a decorated function:

.. code-block:: python
    :emphasize-lines: 1,13,14

    @click.group()
    def cli():
        pass

    @click.command()
    def initdb():
        click.echo('Initialized the database')

    @click.command()
    def dropdb():
        click.echo('Dropped the database')

    cli.add_command(initdb)
    cli.add_command(dropdb)

If your commands share resources, more decorators are used:

.. code-block:: python
    :emphasize-lines: 15,22

    import os
    import click


    class Repo(object):
        def __init__(self, home=None, debug=False):
            self.home = os.path.abspath(home or '.')
            self.debug = debug


    @click.group()
    @click.option('--repo-home', envvar='REPO_HOME', default='.repo')
    @click.option('--debug/--no-debug', default=False,
                  envvar='REPO_DEBUG')
    @click.pass_context
    def cli(ctx, repo_home, debug):
        ctx.obj = Repo(repo_home, debug)

    @cli.command()
    @click.argument('src')
    @click.argument('dest', required=False)
    @click.pass_obj
    def clone(repo, src, dest):
        pass

Click allows unlimited command nesting and can do eveything argparse can.

However, it has several disadvantages:

    -   When one function has four decorators, readability suffers.
    -   Grouping functions is done with custom functions, whereas classes are a more natural way to group functions.
    -   Because all commands and groups are global functions, there's no obvious way to extend CLI.
    -   Sharing resources is complicated.

Cliar
=====

In Cliar, a command-line interface is an ordinary class, a subclass of ``cliar.CLI``. Every non-underscored method of this class is a command. Parameters of a method are arguments of the corresponding command. Method's docstring is command's help text::

    from cliar import CLI


    class MyCLI(CLI):
        def hello(self, name, count=1):
            '''Simple program that greets NAME for a total of COUNT times.'''
            
            for x in range(count):
                print('Hello %s!' % name)


    if __name__ == '__main__':
        MyCLI()

Root level args are params of the special ``_root`` method. Global state is stored in the ``self`` variable, just like in any other normal class.

.. code-block:: python
    :emphasize-lines: 5,8,13

    from cliar import CLI


    class MyCLI(CLI):
        def _root(self, verbose=False):
            '''This method is executed before any command'''
            
            self.verbose = verbose

        def hello(self, name, count=1):
            '''Simple program that greets NAME for a total of COUNT times.'''
            
            if self.verbose:
                print('This is verbose')

            for x in range(count):
                print('Hello %s!' % name)


    if __name__ == '__main__':
        MyCLI()

Because all commands are just methods of a class, extending a CLI is as easy as subclassing:

.. code-block:: python
    :caption: cli.py

    from cliar import CLI


    class MyCLI(CLI):
        def command1(self, name='Guido'):
            '''Base command'''

            print('Hello, ', name)

.. code-block:: python
    :caption: cli_extension.py

    from cli import MyCLI


    class MyCLIExtension(MyCLI):
        def command2(self, food='Spam'):
            '''Extension command'''
            
            print(food, ' is delicious!')


    if __name__ == '__main__':
        MyCLIExtension()

.. code-block:: bash
    
    $ ./cli_extension.py -h
    usage: ecli.py [-h] {command2,command1} ...

    optional arguments:
      -h, --help           show this help message and exit

    commands:
      {command2,command1}  available commands
        command2           Extension command
        command1           Base command

    $ ./cli_extension.py command1
    Hello,  Guido

    $ ./cli_extension.py command2
    Spam  is delicious!


Unlike Click, Cliar doesn't allow third-level commands. Generally, Cliar is much less powerful than Click.

If you need a quick way to create a CLI with minumum code and room for extendability, use Cliar.

If you don't care about extendability, but really need to edit the metavar, Click is the way to go.