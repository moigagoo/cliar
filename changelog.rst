1.0.0
=====

-   First version. Changelog started.

1.0.1
=====

-   Alias support added with the "add_aliases" decorator.

1.0.2
=====

-   Docstring added to the add_aliases function.
-   The set_name function is now less hacky.

1.0.3
=====

-   Python 2 support added.

1.0.4
=====

-   Nested CLI methods would not override parent methods. Fixed.

1.0.5
=====

-   The ``ignore`` decorator added to exclude a method from being converted into a command.

1.0.6
=====

-   Command-line args are now parsed by explicitly calling the ``.parse()`` method.

1.0.7
=====

-   Support of multiple values for a single arg added.

1.0.8
=====

-   Description and help texts now preserve line breaks from docstrings.

1.0.9
=====

-   Commands now use the first docstring line as help and the whole docstring as description.

1.1.0
=====

-   Command descriptions did not preserve line breaks from docstrings. Fixed.

1.1.1
=====

-   Python 2: If only the _root handler was defined, a "too few agruments" error raised. Fixed.
-   If only the _root handler is defined, the commands subparser is not added anymore.
-   Packaging improved, the installation package now includes both Python 2 and 3 sources.

1.1.2
=====

-   Setup: Python version check improved.

1.1.3
=====

-   Code cleanup.

1.1.4
=====

-   Code improvements for API documentation.

1.1.5
=====

-   Optional arguments are now prepended with '--', not '-'.
-   Short argument names are now generated from the long ones: ``name`` handler arg corresponds to ``-n`` and ``--name`` commandline args.
-   Python 2 support dropped. Python 3.5+ required.
-   Code refactored, type hints added.


1.1.6
=====

-   Underscores in handler names are now replaced with dashes when the corresponding command name is generated.
