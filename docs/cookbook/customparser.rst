******************
Custom Arg Parsers
******************

.. note:: This example works in Python 3 only.

Arg type can be any Python callable that accepts a string, including custom functions. `Read more <https://docs.python.org/3/library/argparse.html#type>`__ in the argparse docs.

:download:`Download source <customparser.py>`

.. literalinclude:: customparser.py

Usage:

.. code-block:: bash

    $ python customparser.py 
    usage: customparser.py [-h] {personify} ...

    This CLI demonstrates the usage
    of a custom arg parser.
        
    optional arguments:
      -h, --help   show this help message and exit

    commands:
      {personify}  Available commands:
        personify  This method uses a custom ``string_to_person``
                    parser to convert input string into a ``Person`` instance
                    *before* handling it.

    $ python customparser.py personify -h
    usage: customparser.py personify [-h] person

    This method uses a custom ``string_to_person``
    parser to convert input string into a ``Person`` instance
    *before* handling it.        

    positional arguments:
      person

    optional arguments:
      -h, --help  show this help message and exit

    $ python customparser.py personify "Abe Lincoln"
    First name: Abe
    Last name: Lincoln

    $ python customparser.py personify "Guido van Rossum"
    Conversion failed # Sorry, Guido!

    $ python customparser.py personify 42
    Conversion failed
