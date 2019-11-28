from cliar import Cliar


class MultiwordArgs(Cliar):
    def say(self, words_to_say: str, to_upper=False, repeat_words: int = 1):
        for _ in range(repeat_words):
            if to_upper:
                print(words_to_say.upper())
            else:
                print(words_to_say)

if __name__ == "__main__":
    MultiwordArgs().parse()
