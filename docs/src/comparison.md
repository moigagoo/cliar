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

You want the usage to be something like this:

```shell
$ player play file.mp3          # Core functionality
$ pip install player.ext.seek   # Install extension
$ player seek 1:23              # Extension-provided functionality
```

This approach has several benefits:

-   the user will be able to install only the parts they need
-   you will be able to delegate most of the work on the player to the community
-   if you add functionality to the player yourself, you'll use the same API as third-party developers, i.e. eat your own dog food, which makes for better APIs

So, your job is provide a way for third parties to add commands to the basic CLI and override existing commands.
