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