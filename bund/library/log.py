import logging, coloredlogs
from bund.library.ns import nsGet, nsSet

def logInit(namespace, level='INFO'):
    id = nsGet(namespace, "/sys/id", None)
    if id is None:
        nsSet(namespace, "/sys/log/ready", False)
        return namespace
    logger = logging.getLogger(id)
    nsSet(namespace, "/sys/log/level", level)
    nsSet(namespace, "/sys/log/logger", logger)
    coloredlogs.install(fmt="%(asctime)s [%(levelname)s] %(message)s", milliseconds=True, level=level, logger=logger)
    nsSet(namespace, "/sys/log/ready", True)
    return namespace

def debug(namespace, fmt, **kw):
    logger = nsGet(namespace, "/sys/log/logger", None)
    if logger is not None:
        logger.debug(fmt % kw)

def warning(namespace, fmt, **kw):
    logger = nsGet(namespace, "/sys/log/logger", None)
    if logger is not None:
        logger.warning(fmt % kw)

def info(namespace, fmt, **kw):
    logger = nsGet(namespace, "/sys/log/logger", None)
    if logger is not None:
        logger.info(fmt % kw)

def error(namespace, fmt, **kw):
    logger = nsGet(namespace, "/sys/log/logger", None)
    if logger is not None:
        logger.error(fmt % kw)

def critical(namespace, fmt, **kw):
    logger = nsGet(namespace, "/sys/log/logger", None)
    if logger is not None:
        logger.critical(fmt % kw)
