#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年8月11日@
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Utils.Project
@description: 项目实体类
"""
import os
import pickle
import shutil
import time

from Utils import Constant
from Utils.Tools import log


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class Project:

    def __init__(self, name, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)
        self._name = os.path.splitext(name)[0]  # 项目名称
        self._uiFiles = set()  # 项目中包含的UI文件路径
        # 储存项目缩略图的文件夹
        self._dir = os.path.abspath(os.path.join(
            Constant.BaseDir, 'Projects', self._name))
        # 项目文件
        self._proFile = self._dir + '.project'
        # 样式文件
        self._styleFile = self._dir + '.qss'
        # 样式内容
        self._styleSheet = ''

    def __str__(self):
        return 'name:{}, time:{}, style length:{}'.format(self.name, self.time, len(self._styleSheet))

    @property
    def name(self):
        """项目名"""
        return self._name

    @property
    def time(self):
        """修改时间"""
        if not os.path.isfile(self._proFile) or not os.path.exists(self._proFile):
            return ''
        return time.strftime('%Y/%m/%d-%H:%M:%S', time.localtime(os.path.getmtime(self._proFile)))

    @property
    def dirPath(self):
        """返回预览图储存路径文件夹"""
        return self._dir

    @property
    def proFile(self):
        """返回项目文件路径"""
        return self._proFile

    @property
    def styleFile(self):
        """返回样式文件路径"""
        return self._styleFile

    @property
    def styleSheet(self):
        """返回样式字符串"""
        return self._styleSheet

    @property
    def uiFiles(self):
        """获取所有UI文件路径"""
        return self._uiFiles

    def add(self, file):
        """添加UI文件
        :param file: ui文件
        """
        self._uiFiles.add(file)

    def create(self):
        """创建项目"""
        # 判断文件是否存在
        if os.path.isfile(self._proFile) and os.path.exists(self._proFile):
            return 0
        # 创建图片目录
        os.makedirs(self._dir, exist_ok=True)
        # 创建空的样式文件
        open(self._styleFile, 'wb').write(Constant.QssHeader)
        # 创建配置文件
        pickle.dump(set(), open(self._proFile, 'wb'))
        return 1

    def load(self):
        """加载项目"""
        try:
            # 加载保存的ui文件路径
            self._uiFiles = pickle.load(open(self._proFile, 'rb'))
            # 加载样式内容
            self._styleSheet = open(
                self._styleFile, 'rb').read().decode(encoding='utf-8')
            return
        except Exception as e:
            log.error(str(e))
            return str(e.args)

    def save(self):
        """保存改动"""
        try:
            # 保存样式文件
            open(self._styleFile, 'wb').write(
                self._styleSheet.encode(encoding='utf_8'))
            # 保存UI路径
            pickle.dump(self._uiFiles, open(self._proFile, 'wb'))
            return
        except Exception as e:
            log.error(str(e))
            return str(e.args)

    def delete(self):
        """删除项目"""
        try:
            # 删除项目文件
            os.unlink(self._proFile)
            # 删除样式文件
            os.unlink(self._styleFile)
            # 删除预览图目录
            shutil.rmtree(self._dir)
            return
        except Exception as e:
            log.error(str(e))
            return str(e.args)
