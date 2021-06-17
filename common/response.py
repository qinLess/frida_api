# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: response.py
    Time: 2020/5/10 12:42 下午
-------------------------------------------------
    Change Activity: 2020/5/10 12:42 下午
-------------------------------------------------
"""
import time

from flask_restful import abort


def generate_response(data=None, kind=None, desc='失败'):
    return {
        'desc': desc,
        'kind': kind,
        'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
        'data': data
    }


def my_abort(http_status_code, **kwargs):
    if http_status_code == 400:
        abort(400, **generate_response(data=kwargs.get('message')))

    abort(http_status_code)
