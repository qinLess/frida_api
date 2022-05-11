# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: test.py
    Time: 2021/3/25 下午4:52
-------------------------------------------------
    Change Activity: 2021/3/25 下午4:52
-------------------------------------------------
    Desc: 
"""
from flask_restful import Resource


class Test(Resource):

    def get(self):
        return 'Hello World!'
