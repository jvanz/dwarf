import os

from distutils.core import setup

NAME = 'web_graph'
DESCRIPTION = 'Web graph service'
URL = 'https://github.com/jvanz/dwarf'
EMAIL = 'guilherme.sft@gmail.com'
AUTHOR = 'Jose Guilherme Vanz'

#  What packages are required for this module to be executed?
REQUIRED = [
#  'requests', 'maya', 'records',
]


here = os.path.abspath(os.path.dirname(__file__))


setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=["web_graph"],
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
)

