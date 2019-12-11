# 1.3.4 (December 11, 2019)

-   Add support for async handlers (per [#13](https://github.com/moigagoo/cliar/pull/13)).


# 1.3.3 (November 29, 2019)

-   Fix [#11](https://github.com/moigagoo/cliar/issues/11): multiword optional args of any type other than `bool` couldn't be used.


# 1.3.2 (July 23, 2019)

-   Global args are now stored in `self.global_args` instead of `self._root_args`.
-   Global args are now available in nested commands. [Read more](https://moigagoo.github.io/cliar/tutorial/#global-arguments).


# 1.3.1 (July 22, 2019) [Removed from PyPI]

-   Commands can now access root command args via `self._root_args`. [Read more](https://moigagoo.github.io/cliar/tutorial/#root-command).


# 1.3.0 (July 21, 2019)

-   Add support for nested commands. [Read more](https://moigagoo.github.io/cliar/tutorial/#nested-commands).
-   Fix incorrect mapping from handler params to optional CLI args.


# 1.2.5 (June 30, 2019)

-   Prepare for postponed annotation evaluation, which will be the default in Python 4.0 (see #2).

# 1.2.4 (June 27, 2019)

-   Add `show_defaults` param to `set_help` util. [Read more](https://moigagoo.github.io/cliar/tutorial/#argument-descriptions).

# 1.2.3 (May 13, 2019)

-   Fix Python 3.7 incompatibility.
-   Add `set_sharg_map` to override or disable short arg names.

# 1.2.2 (June 3, 2018)

-   Make `_root` not an abstract method.

# 1.2.1 (June 2, 2018)

-   Fix critical bug that disallowed string params.

# 1.2.0 (June 1, 2018)

-   Boolean handler params are converted into `store_true` arguments. Before that, params with default value of `True` were much confusingly converted into `store_false` arguments.
-   Support `List[int]` and similar arg types. If the param type is a subclass of `typing.Iterable` and has a type specified in brackets, it's converted into multivalue arg of the type in the brackets.
-   Do not print help whenever `_root` command is invoked.
-   Convert the `cliar` module into a package.
-   Add tests.
-   Switch to Poetry.

# 1.1.9

-   Add the ability to set help messages for arguments.
-   Add the ability to set metavars for arguments.

# 1.1.8

-   **[Breaks backward compatibility]** Base CLI class renamed from `CLI` to `Cliar`.
-   Fixed a bug where commandline args with dashes weren't mapped to corresponding param names with underscores.

# 1.1.7

-   Add the ability to override mapping between commandline args and and handler params. By default, handler params correspond to args of the same name with underscores replaced with dashes.

# 1.1.6

-   Underscores in handler names are now replaced with dashes when the corresponding command name is generated.

# 1.1.5

-   Optional arguments are now prepended with '--', not '-'.
-   Short argument names are now generated from the long ones: `name` handler arg corresponds to `-n` and `--name` commandline args.
-   Python 2 support dropped. Python 3.5+ required.
-   Code refactored, type hints added.

# 1.1.4

-   Code improvements for API documentation.

# 1.1.3

-   Code cleanup.

# 1.1.2

-   Setup: Python version check improved.

# 1.1.1

-   Python 2: If only the _root handler was defined, a "too few agruments" error raised. Fixed.
-   If only the _root handler is defined, the commands subparser is not added anymore.
-   Packaging improved, the installation package now includes both Python 2 and 3 sources.

# 1.1.0

-   Command descriptions did not preserve line breaks from docstrings. Fixed.

# 1.0.9

-   Commands now use the first docstring line as help and the whole docstring as description.

# 1.0.8

-   Description and help texts now preserve line breaks from docstrings.

# 1.0.7

-   Support of multiple values for a single arg added.

# 1.0.6

-   Command-line args are now parsed by explicitly calling the `.parse()` method.

# 1.0.5

-   The `ignore` decorator added to exclude a method from being converted into a command.

# 1.0.4

-   Nested CLI methods would not override parent methods. Fixed.

# 1.0.3

-   Python 2 support added.

# 1.0.2

-   Docstring added to the add_aliases function.
-   The set_name function is now less hacky.

# 1.0.1

-   Alias support added with the "add_aliases" decorator.

# 1.0.0

-   First version. Changelog started.
