# Cliar vs. Click vs. docopt

Name | DSL-based | Casts arg types | Extensible | Testable without shell exec | Has pun in name
---- | --------- | --------------- | ---------- | --------------------------- | ---------------
[Cliar](https://moigagoo.github.io/cliar/) | ❌ | ✔ | ✔, *in* third-party modules and *with* third-party modules | ✔ | ✔
[Click](http://click.pocoo.org/) | ❌ | ❌ | ✔, in third-party modules | ❌ | ✔
[docopt](http://docopt.org/) | ✔  | ❌ | ❌ | ❌ | ❌
[argparse](https://docs.python.org/3/library/argparse.html) | ❌ | ❌ | ❌ | ❌ | ❌
