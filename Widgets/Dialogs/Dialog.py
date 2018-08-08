#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ctypes.wintypes

from PyQt5.QtWidgets import QDialog


# Created on 2018年8月8日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Core.Dialog
# description:
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0

WM_NCACTIVATE = 0x0086


class Dialog:

    BorderWidget = None  # 边框闪烁的控件

    def doMoveWindow(self, pos):
        if self.isMaximized() or self.isFullScreen():
            return
        # 移动窗口
        self.move(self.x() + pos.x(), self.y() + pos.y())

    def activeAnimation(self, actived):
        """边框闪烁动画
        :param actived: 是否激活
        """
        # 修改控件的自定义属性
        self.BorderWidget.setProperty('active', actived)
        # 刷新它的样式
        self.style().polish(self.BorderWidget)

    def nativeEvent(self, eventType, message):
        retval, result = QDialog.nativeEvent(self, eventType, message)
        if eventType == 'windows_generic_MSG' and self.BorderWidget:
            msg = ctypes.wintypes.MSG.from_address(message.__int__())
            if msg.message == WM_NCACTIVATE:
                # 绘制模态窗口的边框效果
                self.activeAnimation(msg.wParam == 1)
        return retval, result
