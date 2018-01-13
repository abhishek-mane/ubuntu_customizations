'''
    * Logger initialization module
'''

import logging.config
import logging as logger
from colors import COLORS

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


def Print(head, msg):
    logger.info("%s[%s] : %s%s" % (COLORS.HEADINGS, head, msg, COLORS.RESET))