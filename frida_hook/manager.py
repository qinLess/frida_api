# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: manager.py
    Time: 2021/4/4 下午9:49
-------------------------------------------------
    Change Activity: 2021/4/4 下午9:49
-------------------------------------------------
    Desc: 
"""
import threading

import frida
import os
import time
import random
import re

from common.log_setting import get_logger
from frida_hook.devices import HookDevice

logger = get_logger("manager")


class Devices(object):

    @staticmethod
    def get_devices():
        output = os.popen("adb devices").read()
        devices = re.findall(r"\n(.+?)device", output, re.M | re.S | re.I)
        devices = [
            device.replace("\n", "").replace("\t", "").strip() for device in devices
        ]

        logger.info(f'远程设备列表: {devices}')

        return [Devices.connect_device(device) for device in devices]

    @staticmethod
    def connect_device(host):
        try:
            process = frida.get_device(host, timeout=10)
            logger.debug(f'设备连接成功: {host} {process}')
            return process

        except frida.TransportError as e:
            logger.info(f'frida 连接超时: {host} {e}')
            time.sleep(1)
            return Devices.connect_device(host)

        except frida.ServerNotRunningError as e:
            if 'unable to connect to remote frida-server: closed' in e.args:
                logger.info(f'frida-server 未启动: {host} {e}')

            elif 'unable to connect to remote frida-server' in e.args:
                logger.info(f'连接远程 frida 失败，尝试端口转发: {host} {e}')

                os.system(f'adb -s {host} forward tcp:27042 tcp:27042')
                return Devices.connect_device(host)


device_list = Devices.get_devices()


def get_device_instance(kwargs):
    if len(kwargs['process_list']) == 0:
        kwargs['process_list'] = [HookDevice(device=device, kwargs=kwargs) for device in device_list]

    process = random.choice(kwargs['process_list'])

    logger.debug(f'attach {kwargs["app_name"]}: {process.device}')

    if not process.device:
        return get_device_instance(**kwargs)

    if not process.script:
        mutex = threading.Lock()
        mutex.acquire()
        process.new_script()
        mutex.release()

    return process
