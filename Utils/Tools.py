#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018年7月16日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Utils.Tools
@description:
"""

import logging
import os

from PyQt5.QtCore import QFile, QIODevice, QTextStream, QTextCodec


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


def readData(path):
    """red file data"""
    file = QFile(path)
    if not file.open(QIODevice.ReadOnly):
        log.warn('read file error')
        return
    stream = QTextStream(file)
    stream.setCodec(QTextCodec.codecForName('UTF-8'))
    data = stream.readAll()
    file.close()
    del stream
    return data


def initLog(name, file=None, level=logging.ERROR, formatter=None):
    formatter = formatter or logging.Formatter(
        '[%(asctime)s %(name)s %(module)s:%(funcName)s:%(lineno)s] %(levelname)-8s %(message)s'
        if level == logging.DEBUG else '[%(asctime)s %(name)s] %(levelname)-8s %(message)s')

    logger = logging.getLogger(name)
    logger.setLevel(level)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file = os.path.abspath(file)
    if file:
        file_handler = logging.FileHandler(file, mode='w')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


log = logging.getLogger('QtSkin')
