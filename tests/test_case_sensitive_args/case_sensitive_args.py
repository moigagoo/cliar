from cliar import Cliar, set_sharg_map


class CaseSensitiveArgs(Cliar):
    @set_sharg_map({'url': None, 'username': 'U'})
    def _root(self, unique='', url='', username=''):
        pass


if __name__ == "__main__":
    CaseSensitiveArgs().parse()
