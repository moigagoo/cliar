from cliar import Cliar, set_arg_map, set_sharg_map


class GlobalArgs(Cliar):
    @set_arg_map({'user': 'as'})
    @set_sharg_map({'user': None})
    def _root(self, user='', password=''):
        pass

    def connect(self, host: str):
        user = self._root_args["as"]
        password = self._root_args["password"]

        print(f'Connecting to {host}, user="{user}", password="{password}"')


GlobalArgs().parse()
