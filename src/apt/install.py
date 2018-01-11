'''
    * Installs a specified package
'''

import os
import config

# define print function
Print = config.Print

COMMAND = "sudo apt-get install %s -y"

def install(pkg):
    Print(__name__, 'Installing package %s...' % (pkg))
    os.system(COMMAND % (pkg))