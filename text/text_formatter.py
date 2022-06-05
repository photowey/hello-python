# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file text_formatter
# @description text_formatter
# @author photowey
# @date 2022/06/06
# ---------------------------------------------


class Formatter(object):

    @staticmethod
    def text_format(text: str, *args) -> str:
        return text.format(*args)
