import pkgutil
from rocker.extensions import RockerExtension


class ViFi(RockerExtension):

    name = 'vifi'

    @classmethod
    def get_name(cls):
        return cls.name

    def __init__(self):
        self.name = ViFi.get_name()

    def get_snippet(self, cliargs):
        snippet = pkgutil.get_data('rocker_plugins', 'snippets/{}_snippet.Dockerfile'.format(self.name)).decode('utf-8')
        return snippet

    @staticmethod
    def register_arguments(parser, defaults={}):
        parser.add_argument('--mp-vifi',
            action='store_true',
            help='install vim and fish with apt')
