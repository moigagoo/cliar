*******************
Python 2 Disclaimer
*******************

I don't like Python 2. Cliar was initially written in Python 3 and relies on features first introduced in 3.3:

    -   function annotations to check arg types
    -   the ``inspect.signature`` function create CLI commands
    -   the ``aliases`` param for the ``add_subparsers`` function to define command aliases

However, it was necessary to backport Cliar to Python 2, and so I did:

    -   arg types can be inferred only from teh default values
    -   ``inspect.getargspec`` is used to work around ``inspect.signature`` absence
    -   command aliases are not supported

Yes, the Python 2 version is worse than the Python 3 one, and I believe this is fair. I believe, Python 3 is a better language, though supporting Python 2 is unavoidable because server distros like Debian or CentOS refuse to ship newer Python versions.

Coding is my happy place, and coding in Python 3 is just so much more fun. I'm happy to extend the Cliar functionality in Python 3, but I'll backport only the bare minumum to Python 2, because of how painful and boring it is.

If you are interested in backporting Cliar to Python 2, feel free to `fork the project <https://bitbucket.org/moigagoo/cliar/fork>`__  and submit pull requests.