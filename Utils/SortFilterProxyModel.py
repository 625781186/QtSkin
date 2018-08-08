#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import QSortFilterProxyModel, Qt


# Created on 2018年8月7日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Core.SortFilterProxyModel
# description: QListView排序模型
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class SortFilterProxyModel(QSortFilterProxyModel):

    def lessThan(self, source_left, source_right):
        if not source_left.isValid() or not source_right.isValid():
            return False
        # 获取数据
        leftData = self.sourceModel().data(source_left)
        rightData = self.sourceModel().data(source_right)
        if self.sortOrder() == Qt.DescendingOrder:
            # 按照时间倒序排序
            leftData = leftData.split('-')[-1]
            rightData = rightData.split('-')[-1]
            return leftData > rightData
#         elif self.sortOrder() == Qt.AscendingOrder:
#             #按照名字升序排序
#             leftData = leftData.split('-')[0]
#             rightData = rightData.split('-')[0]
#             return leftData < rightData
        return super(SortFilterProxyModel, self).lessThan(source_left, source_right)
