# -*- coding: utf-8 -*-
"""
@author: qinLess
@file: config.py
@time: 2020/4/17 1:56 下午
"""


class Config:
    HOST = '0.0.0.0'
    PORT = 6999


class Product(Config):
    pass


config = {
    'product': Product
}

config = config['product']
