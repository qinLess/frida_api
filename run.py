# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: run.py
    Time: 2021/3/25 下午4:49
-------------------------------------------------
    Change Activity: 2021/3/25 下午4:49
-------------------------------------------------
    Desc: 
"""
import flask_restful
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from config import config

from common.response import my_abort

app = Flask(__name__)
api = Api(app)
cors = CORS(app, allow_headers='Content-Type', CORS_SEND_WILDCARD=True, resources='/*')
flask_restful.abort = my_abort

app.config.from_object(config)

app.extensions['api_config'] = config

app_ctx = app.app_context()
app_ctx.push()

from resources.test import Test
from resources.zs_xq.send_message import ZSXQSendMessage
from resources.ks.get_sig import KSGetNSSig3, KSGetSig

api.add_resource(Test, '/')
api.add_resource(ZSXQSendMessage, '/zs_xq/sendMessage')

api.add_resource(KSGetSig, '/ks/get_sig')
api.add_resource(KSGetNSSig3, '/ks/get_ns_sig3')

app_ctx.pop()

if __name__ == '__main__':
    app.run(debug=True, host=config.HOST, port=config.PORT)
