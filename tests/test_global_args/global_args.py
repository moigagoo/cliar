from cliar import Cliar, set_arg_map, set_sharg_map

class Utils(Cliar):
    def upload(self, filename: str):
        user = self.global_args['as']
        password = self.global_args['password']

        print(f'Uploading {filename}, user="{user}", password="{password}"')


class GlobalArgs(Cliar):
    utils = Utils

    @set_arg_map({'user': 'as'})
    @set_sharg_map({'user': None})
    def _root(self, user='', password=''):
        pass

    def connect(self, host: str):
        user = self.global_args['as']
        password = self.global_args['password']

        print(f'Connecting to {host}, user="{user}", password="{password}"')


GlobalArgs().parse()
