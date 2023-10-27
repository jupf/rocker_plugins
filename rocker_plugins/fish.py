import pkgutil
from rocker.extensions import RockerExtension


class Fish(RockerExtension):

    name = 'fish'

    @classmethod
    def get_name(cls):
        return cls.name

    def __init__(self):
        self.name = Fish.get_name()

    def get_snippet(self, cliargs):
        snippet = pkgutil.get_data('rocker_plugins', 'snippets/{}_snippet.Dockerfile.em'.format(self.name)).decode('utf-8')
        return snippet

    @staticmethod
    def register_arguments(parser, defaults={}):
        parser.add_argument('--fish',
            action='store_true',
            help='install fish shell with apt')

