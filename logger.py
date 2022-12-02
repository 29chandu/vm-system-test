import logging
from logging.config import dictConfig

from settings import Config

log_config = {
    'version': 1,
    'formatters': {
        'default': {'format': '%(asctime)s - %(levelname)s - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'}
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': 'logs.log',
        }
    },
    'loggers': {
        'default': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    },
    'disable_existing_loggers': False
}


def configure_logger(name='default'):

    log_config['handlers']['console']['level'] = Config.CONSOLE_LOG_LEVEL
    log_config['handlers']['file']['level'] = Config.FILE_LOG_LEVEL
    log_config['handlers']['file']['filename'] = Config.LOG_FILE_PATH

    dictConfig(log_config)
    return logging.getLogger(name)


logger = configure_logger()
