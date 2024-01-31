import pkgutil
from rocker.extensions import RockerExtension


class Nano(RockerExtension):

    name = 'nano'

    @classmethod
    def get_name(cls):
        return cls.name

    def __init__(self):
        self.name = Nano.get_name()

    def get_snippet(self, cliargs):
        snippet = pkgutil.get_data('rocker_plugins', 'snippets/{}.Dockerfile.snippet'.format(self.name)).decode('utf-8')
        return snippet

    @staticmethod
    def register_arguments(parser, defaults={}):
        parser.add_argument('--nano',
            action='store_true',
            help='install nano with apt')
