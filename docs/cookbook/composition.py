from cliar import Cliar


class Base(Cliar):
    def hello(self, name: str):
        print(f'Hello, {name}!')


class ExtensionA(Cliar):
    def say_a(self, number: int = 1):
        print('a' * number)


class ExtensionB(Cliar):
    def say_b(self, capitalize: bool = False):
        if capitalize:
            print('B')
        else:
            print('b')


EXTENSIONS = (ExtensionA, ExtensionB)


class Composed(Base, *EXTENSIONS):
    pass


if __name__ == '__main__':
    Composed().parse()
