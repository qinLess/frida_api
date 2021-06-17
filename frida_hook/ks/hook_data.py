# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: hook_data.py
    Time: 2021/4/4 下午9:47
-------------------------------------------------
    Change Activity: 2021/4/4 下午9:47
-------------------------------------------------
    Desc: 
"""
import os
import functools

from common.log_setting import get_logger
from frida_hook.manager import get_device_instance

script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'script.js')
logger = get_logger("ks_hook_data")

apk_info = {
    # 设备列表（存放设备列表）
    'process_list': [],
    # app 名称
    'app_name': '快手极速版',
    # frida hook js 文件绝对路径
    'script_path': script_path,
    # apk 包名称
    'apk_package_name': 'com.kuaishou.nebula',
    # apk 启动页面名称（用来自动重启 apk）
    'apk_main_activity': 'com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity'
}

process = get_device_instance(apk_info)


def reset_process(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global process
        process = get_device_instance(apk_info)

        return func(*args, **kwargs)

    return wrapper


@reset_process
def get_sig(string):
    try:
        return process.script.exports.getsign(string)

    except Exception as e:
        logger.info(f'get_sig.e: {e}')

        process.reset_script()
        return get_sig(string)


@reset_process
def get_ns_sig3(string):
    try:
        return process.script.exports.getnssign3(string)

    except Exception as e:
        logger.info(f'get_ns_sig3.e: {e}')

        process.reset_script()
        return get_ns_sig3(string)


if __name__ == '__main__':
    pass
