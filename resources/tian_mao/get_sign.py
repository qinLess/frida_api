# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: get_sign.py
    Time: 2021/6/23 下午4:02
-------------------------------------------------
    Change Activity: 2021/6/23 下午4:02
-------------------------------------------------
    Desc: 
"""
from flask_restful import Resource

from common.parsers import VerifyParams
from common.response import generate_response
from frida_hook.tb.hook_data import get_x_sign


class TBGetXSign(Resource):

    @VerifyParams.get_x_sign
    def post(self, params):
        try:
            res = get_x_sign(params)
            return generate_response(desc='成功', data=res)

        except Exception as e:
            return generate_response(desc='失败', data=e)
