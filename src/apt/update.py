'''
    * Update package sources
'''

import os
import config

# define print function
Print = config.Print

COMMAND = "sudo apt-get update"

def update():
    Print(__name__, 'Updating sources...')
    os.system(COMMAND)