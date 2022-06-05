# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file logger
# @description logger
# @author photowey
# @date 2022/06/06
# ---------------------------------------------

import logging
import os
import time
from datetime import datetime


def make_dirs(target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)


class Logger:

    def __init__(self):
        root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        logger_path = os.path.join(root_path + os.sep + 'log')

        make_dirs(logger_path)

        self.log_name = logger_path + os.sep + time.strftime('%Y%m%d%H%M%S') + '.log'
        self.strf_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger('logger')
        logger.setLevel(logging.DEBUG)
        self.logger = logger

    def print_console(self, level, message):
        file_handler = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(filename)s[line:%(lineno)d] - %(levelname)s : %(message)s')

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

        self.switch(level, message)

        self.logger.removeHandler(stream_handler)
        self.logger.removeHandler(file_handler)

    def debug(self, message):
        self.print_console(logging.DEBUG, message)

    def info(self, message):
        self.print_console(logging.INFO, message)

    def warning(self, message):
        self.print_console(logging.WARNING, message)

    def error(self, message):
        self.print_console(logging.ERROR, message)

    def switch(self, level, message):
        handler_map = {
            logging.DEBUG: self.logger.debug,
            logging.INFO: self.logger.info,
            logging.WARNING: self.logger.warning,
            logging.ERROR: self.logger.error
        }
        handler = handler_map.get(level)
        if handler:
            handler(message)
