from rocker.extensions import RockerExtension


class IPC(RockerExtension):
    @staticmethod
    def get_name():
        return 'ipc'

    def __init__(self):
        self.name = IPC.get_name()

    def get_preamble(self, cliargs):
        return ''

    def get_docker_args(self, cliargs):
        args = ''
        ipc = cliargs.get('ipc', None)
        args += ' --ipc %s ' % ipc
        return args

    @staticmethod
    def register_arguments(parser, defaults={}):
        parser.add_argument('--ipc', choices=["host","<IPC-NAMESPACE>"],
            default=defaults.get('ipc', None),
            help="What ipc configuration to use.")
