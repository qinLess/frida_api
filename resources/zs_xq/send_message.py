# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: send_message.py
    Time: 2021/4/4 下午10:03
-------------------------------------------------
    Change Activity: 2021/4/4 下午10:03
-------------------------------------------------
    Desc: 
"""
from flask_restful import Resource

from common.parsers import VerifyParams
from common.response import generate_response

from frida_hook.zs_xq.hook_data import send_message


class ZSXQSendMessage(Resource):

    @VerifyParams.zs_xq_send_message
    def post(self, params):
        try:
            send_message(params)
            return generate_response(desc='发送成功')

        except Exception as e:
            return generate_response(desc='发送失败', data=e)
