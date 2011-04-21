
from distutils.core import setup

packname = 'tarbackup' 

setup( name = packname,
    version = '0.1',
    description = 'Backup Manager',
    scripts = [ 'backup' ],
    author = 'Sebastian Heimann',
    author_email = 'sebastian.heimann@zmaw.de',
)
