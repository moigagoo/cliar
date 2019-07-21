from cliar import Cliar


class MultiwordArgs(Cliar):
    def say(self, words_to_say: str, to_upper=False):
        if to_upper:
            print(words_to_say.upper())
        else:
            print(words_to_say)

if __name__ == "__main__":
    MultiwordArgs().parse()
