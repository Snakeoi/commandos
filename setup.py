try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Mój projekt',
    'author': 'Janusz Skotarczak',
    'url': 'skotarczak.com.pl',
    'download_url': '',
    'author_email': 'skotarczak.janusz@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'commandos'
}

setup(**config)
