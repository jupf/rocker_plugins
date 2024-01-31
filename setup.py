from setuptools import setup

setup(
    name='rocker_plugins',
    version='1.1.0',

    description='Personal rocker plugins',

    author='Julian Pfeifer',
    author_email='jpfeifer@jupf.org',

    packages=['rocker_plugins'],
    package_data={'rocker_plugins': ['snippets/*.snippet']},

    install_requires=[
        'rocker',
    ],

    entry_points={
        'rocker.extensions': [
            'fish = rocker_plugins.fish:Fish',
            'vim = rocker_plugins.vim:Vim',
            'vifi = rocker_plugins.vifi:ViFi',
            'ipc = rocker_plugins.ipc:IPC',
            'nano = rocker_plugins.nano:Nano'
        ]
    },
)

