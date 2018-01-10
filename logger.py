'''
    * Logger initialization module
'''

import logging.config

def initialize():
    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }
        },
        'handlers': {
            'console': {
                'class'         : 'logging.StreamHandler',
                'formatter'     : 'default',
                'stream'        : 'ext://sys.stdout',
                'level'         : 'INFO',
            },
        },
        'root': {
            'level' : 'INFO',
            'handlers': ['console']
        }
    })