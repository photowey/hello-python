# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file handler.py
# @description json handler
# @author photowey
# @date 2022/06/06
# ---------------------------------------------

import json


class JSON(object):
    """
    utilities function of JSON.
    """

    @staticmethod
    def transfer_object(body: object) -> str:
        """
        Serialize the object to a JSON string.\n
        :param body:
        :return:
        """
        return json.dumps(body)

    @staticmethod
    def to_json_string(dict_body: dict) -> str:
        """
        Serialize the dict object to a JSON string.\n
        :param dict_body:
        :return:
        """
        return json.dumps(dict_body)

    @staticmethod
    def to_json_strings(dict_body: list) -> str:
        """
        Serialize the list object to a JSON string.\n
        :param dict_body:
        :return:
        """
        return json.dumps(dict_body)

    @staticmethod
    def to_pretty_json_string(dict_body: dict) -> str:
        """
          Serialize the dict object to a pretty JSON string.\n
          :param dict_body:
          :return:
          """
        return json.dumps(dict_body, sort_keys=True, indent=4)

    @staticmethod
    def to_pretty_json_strings(dict_body: list) -> str:
        """
        Serialize the list object to a pretty JSON string.\n
        :param dict_body:
        :return:
        """
        return json.dumps(dict_body, sort_keys=True, indent=4)

    @staticmethod
    def parse_object(json_str: str) -> dict:
        """
        Deserialize the JSON string into a dict-object.\n
        :param json_str:
        :return:
        """
        return json.loads(json_str)

    @staticmethod
    def parse_array(json_str: str) -> list:
        """
        Deserialize the JSON string into a list-object.\n
        :param json_str:
        :return:
        """
        return json.loads(json_str)
