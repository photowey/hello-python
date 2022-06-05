# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file conftest.py
# @description conftest
# @author photowey
# @date 2022/06/06
# ---------------------------------------------

import pytest

from logger.logger import Logger


@pytest.fixture(
    scope='session',
    autouse=True
)
def logger():
    logger = Logger()
    return logger
