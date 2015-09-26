from distutils.core import setup
from json import loads as json_loads
LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

DETAILS = None
with open('details.json') as file:
    DETAILS = json_loads(file)

setup(
    name = DETAILS.name,
    packages = DETAILS.packages,
    version = DETAILS.version,
    description = DETAILS.description,
    long_description = LONG_DESCRIPTION,
    author = DETAILS.author,
    author_email = DETAILS.author_email,
    url = DETAILS.url,
    license = DETAILS.license,
    platforms = DETAILS.platform
)