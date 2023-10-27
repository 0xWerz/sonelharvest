from logging import getLogger

logger = getLogger(__name__)


def warn(msg: str):
    logger.warning(f'WARNING: {msg}')


def error(msg: str):
    logger.error(f'ERROR: {msg}')


def info(msg: str):
    logger.info(f'INFO: {msg}')
