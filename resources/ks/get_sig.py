# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: get_sig.py
    Time: 2021/4/18 下午4:31
-------------------------------------------------
    Change Activity: 2021/4/18 下午4:31
-------------------------------------------------
    Desc: 
"""
from flask_restful import Resource

from common.parsers import VerifyParams
from common.response import generate_response

from frida_hook.ks.hook_data import get_sig, get_ns_sig3


class KSGetSig(Resource):

    @VerifyParams.get_sig
    def post(self, params):
        try:
            res = get_sig(params['string'])
            return generate_response(desc='成功', data=res)

        except Exception as e:
            return generate_response(desc='失败', data=e)


class KSGetNSSig3(Resource):

    @VerifyParams.get_ns_sig3
    def post(self, params):
        try:
            res = get_ns_sig3(params['string'])
            return generate_response(desc='成功', data=res)

        except Exception as e:
            return generate_response(desc='失败', data=e)
