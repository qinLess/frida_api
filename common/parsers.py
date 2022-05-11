# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: parsers.py
    Time: 2020/5/10 1:31 下午
-------------------------------------------------
    Change Activity: 2020/5/10 1:31 下午
-------------------------------------------------
"""
import json
import functools
from flask import current_app
from flask_restful.reqparse import RequestParser

from common.log_setting import get_logger

api_config = current_app.extensions['api_config']

parser = RequestParser()
log = get_logger('parsers')


class VerifyParams(object):

    @staticmethod
    def zs_xq_send_message(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            api_parser = parser.copy()
            api_parser.add_argument('user_name', type=str, required=True)
            api_parser.add_argument('account_id', type=int, required=True)
            api_parser.add_argument('account_name', type=str, required=True)
            api_parser.add_argument('avatar_url', type=str, required=True)
            api_parser.add_argument('identifier', type=str, required=True)
            api_parser.add_argument('group_id', type=int, required=True)
            api_parser.add_argument('group_name', type=str, required=True)
            api_parser.add_argument('content', type=str, required=True)

            api_args = api_parser.parse_args()
            log.info(f'jd_order_phone.params: {json.dumps(api_args, ensure_ascii=False)}')
            return func(params=api_args, *args, **kwargs)

        return wrapper

    @staticmethod
    def get_ns_sig3(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            api_parser = parser.copy()
            api_parser.add_argument('string', type=str)

            api_args = api_parser.parse_args()
            log.info(f'get_ns_sig3.params: {json.dumps(api_args, ensure_ascii=False)}')
            return func(params=api_args, *args, **kwargs)

        return wrapper

    @staticmethod
    def get_sig(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            api_parser = parser.copy()
            api_parser.add_argument('string', type=str)

            api_args = api_parser.parse_args()
            log.info(f'get_sig.params: {json.dumps(api_args, ensure_ascii=False)}')
            return func(params=api_args, *args, **kwargs)

        return wrapper

    @staticmethod
    def get_x_sign(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            api_parser = parser.copy()
            api_parser.add_argument('string', type=str)

            api_args = api_parser.parse_args()
            log.info(f'get_x_sign.params: {json.dumps(api_args, ensure_ascii=False)}')
            return func(params=api_args, *args, **kwargs)

        return wrapper
