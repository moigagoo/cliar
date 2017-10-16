from cliar import CLI


class Base(CLI):
    def hello(self, name: str):
        print(f'Hello, {name}!')


class ExtensionA(CLI):
    def say_a(self, number: int = 1):
        print('a' * number)


class ExtensionB(CLI):
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
