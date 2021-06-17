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
logger = get_logger("zs_xq_hook_data")

apk_info = {
    'process_list': [],
    'app_name': '知识星球',
    'script_path': script_path,
    'apk_package_name': 'com.unnoo.quan',
    'apk_main_activity': 'com.unnoo.quan/.activities.MainActivity'
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
def send_message(message_info):
    try:
        return process.script.exports.sendmessage(message_info)

    except Exception as e:
        logger.info(f'send_message.e: {e}')

        process.reset_script()
        return send_message(message_info)


if __name__ == '__main__':
    pass
