#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年3月29日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: 转换UI文件
@description: 
"""


import os
import sys
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"

path = 'UiFiles'

for name in os.listdir(path):
    fname, ext = os.path.splitext(name)
    if ext == '.ui':
        dst = os.path.abspath(os.path.join(path, 'Ui_' + fname + '.py'))
        command = '{0} -m PyQt5.uic.pyuic --from-imports -x -o {1} {2}'.format(
            sys.executable,
            dst,
            os.path.abspath(os.path.join(path, name))
        )
        print(command)
        os.system(command)
