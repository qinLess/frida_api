# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: devices.py
    Time: 2020/11/6 12:13 下午
-------------------------------------------------
    Change Activity: 2020/11/6 12:13 下午
-------------------------------------------------
    Desc: 
"""
import os
import subprocess

import frida

from common.log_setting import get_logger

logger = get_logger("hook_device")


class HookDevice(object):
    def __init__(self, device=None, kwargs=None, script=None):
        self.device = device
        self.script = script

        self.script_path = kwargs.get('script_path')
        self.apk_package_name = kwargs.get('apk_package_name')
        self.apk_main_activity = kwargs.get('apk_main_activity')

        with open(f'{self.script_path}', 'r', encoding='utf-8') as f:
            self.js_code = f.read()

        self.status_script = 1
        self.attach_app_num = 1
        self.reset_script_num = 1

        self.new_script()

    def reset_script(self):
        self.script = None
        self.new_script()

    def start_app(self):
        try:
            os.system(f'adb -s {self.device.id} shell am start -W -n {self.apk_main_activity}')

        except Exception as e:
            logger.error(f'start_app: {self.device.id} {e}')

    def start_frida(self):
        try:
            cmd = ['adb', '-s', self.device.id, 'shell']
            pipe = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            pipe.stdin.write('su\n'.encode('utf-8'))
            pipe.stdin.write('cd /data/local/tmp/\n'.encode('utf-8'))
            pipe.stdin.write('./frida-server &\n'.encode('utf-8'))
            pipe.stdin.write('exit\n'.encode('utf-8'))

            pipe.communicate(timeout=1)

        except Exception as e:
            logger.error(f'start_frida: {self.device.id} {e}')

    def new_script(self):
        if self.script:
            return True

        try:
            process_pid = self.device.attach(self.apk_package_name)
            script = process_pid.create_script(self.js_code)
            # script.on('message', '')
            script.load()
            logger.debug(f'hook 成功: {self.device.id} {process_pid}')
            self.script = script
            return True

        except frida.ProcessNotFoundError as e:
            logger.error(f'app未启动: {self.device.id} {e}')
            self.start_app()

            if self.status_script == 1:
                self.status_script += 1
                return self.new_script()

        except frida.ServerNotRunningError as e:
            if 'unable to connect to remote frida-server: closed' in e.args:
                logger.error(f'frida-server 未启动: {self.device.id} {e}')

                self.start_frida()
                return self.new_script()

        except frida.NotSupportedError as e:
            logger.error(f'attach app 失败, 重试: {self.device.id} {e}')

            if self.attach_app_num == 1:
                self.attach_app_num += 1

                self.start_app()
                self.new_script()
