'''
    * Logger initialization module
'''

import logging.config
import logging as logger


def initialize():
    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(message)s',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext://sys.stdout',
                'level': 'INFO',
            },
        },
        'root': {
            'level': 'INFO',
            'handlers': ['console']
        }
    })


def log(head, msg):
    logger.info(head + ' : ' + msg)
