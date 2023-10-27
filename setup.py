from setuptools import setup

setup(
    name='rocker_plugins',
    version='1.0.0',

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
            'fish = mp_rocker.fish:Fish',
            'vim = mp_rocker.vim:Vim',
            'vifi = mp_rocker.vifi:ViFi',
        ]
    },
)

