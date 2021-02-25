# -*- coding: utf-8 -*-
"""This module contains utilities to set up loggers."""
import logging

import hashcode

_DEFAULT_LOG_FORMAT = "[%(asctime)s][%(name)s][%(funcName)s][%(levelname)s] %(message)s"


def setup_logger():
    """Set up the default logger."""
    logger = logging.getLogger(hashcode.__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(_DEFAULT_LOG_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
