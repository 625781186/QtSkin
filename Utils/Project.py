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
        self._files = set()  # 项目中包含的UI文件路径
        # 储存项目缩略图的文件夹
        self._dir = os.path.abspath(os.path.join(
            Constant.BaseDir, 'Projects', self._name))
        # 项目文件
        self._file = self._dir + '.project'

    def __str__(self):
        return 'name:{}, time:{}'.format(self.name, self.time)

    @property
    def name(self):
        """项目名"""
        return self._name

    @property
    def time(self):
        """修改时间"""
        if not os.path.isfile(self._file) or not os.path.exists(self._file):
            return ''
        return time.strftime('%Y/%m/%d-%H:%M:%S', time.localtime(os.path.getmtime(self._file)))

    @property
    def files(self):
        """获取所有UI文件路径"""
        return self._files

    def add(self, file):
        """添加UI文件
        :param file: ui文件
        """
        self._files.add(file)

    def create(self):
        """创建项目"""
        # 判断文件是否存在
        if os.path.isfile(self._file) and os.path.exists(self._file):
            return 0
        # 创建图片目录
        os.makedirs(self._dir, exist_ok=True)
        # 创建配置文件
        pickle.dump(set(), open(self._file, 'wb'))
        return 1

    def load(self):
        """加载项目"""
        try:
            self._files = pickle.load(open(self._file, 'rb'))
            return
        except Exception as e:
            log.error(str(e))
            return str(e.args)

    def save(self):
        """保存改动"""
        try:
            pickle.dump(self._files, open(self._file, 'wb'))
            return
        except Exception as e:
            log.error(str(e))
            return str(e.args)
