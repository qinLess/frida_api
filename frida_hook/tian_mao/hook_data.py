# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: hook_data.py
    Time: 2021/6/23 下午3:58
-------------------------------------------------
    Change Activity: 2021/6/23 下午3:58
-------------------------------------------------
    Desc: 
"""
import os
import functools

from common.log_setting import get_logger
from frida_hook.manager import get_device_instance

script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'script.js')
logger = get_logger('tb_hook_data')

apk_info = {
    'process_list': [],
    'app_name': '天猫',
    'script_path': script_path,
    'apk_package_name': 'com.tmall.wireless',
    'apk_main_activity': 'com.tmall.wireless/.activities.MainActivity'
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
def get_x_sign(params):
    try:
        return process.script.exports.getxsign(params)

    except Exception as e:
        logger.info(f'get_x_sign.e: {e}')

        # process.reset_script()
        # return get_x_sign(params)


if __name__ == '__main__':
    print(get_x_sign(''))
