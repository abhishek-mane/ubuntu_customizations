'''
    * Add ppa source
'''

import os
import config

# define print function
Print = config.Print

COMMAND = "sudo add-apt-repository %s -y"


def add(ppa):
    Print(__name__, 'Adding repository => [%s]' % (ppa))
    os.system(COMMAND % (ppa))
