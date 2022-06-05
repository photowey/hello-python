# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_reader.py
# @description test_reader
# @author photowey
# @date 2022/06/06
# ---------------------------------------------

import os

import pytest
import requests

from yamlx.reader import YmlReader

yml_path = os.path.join(os.getcwd() + '{}tests{}resources{}test_yml.yml'.format(os.sep, os.sep, os.sep))

reader = YmlReader(yml_path)
content = reader.read_yml()


class TestYmlReader:
    """
    test yml reader
    """

    @pytest.mark.parametrize('context', content)
    def test_yml_reader(self, context, logger):
        url = context['request']['url']
        parameters = context['request']['parameters']
        response = requests.get(url=url, params=parameters)
        html = response.content.decode("utf-8")
        logger.info('request: url:[{}]'.format(url))
        logger.info('response: status_code:[{}], html:\n{}'.format(response.status_code, html))
