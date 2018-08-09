#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018年8月4日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.Menus.ShareMenu
@description: 底部分享菜单
"""

from PyQt5.QtCore import QPropertyAnimation, QPoint
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMenu


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class ShareMenu(QMenu):

    def __init__(self, *args, **kwargs):
        super(ShareMenu, self).__init__(*args, **kwargs)
        self.addAction(self.tr('分享到微博'), self.shareToWb)
        self.addAction(self.tr('分享到微信'), self.shareToWx)
        # 动画效果
        self.fadeAnimation = QPropertyAnimation(self, b'pos')
        # 持续时间
        self.fadeAnimation.setDuration(200)

    def shareToWb(self):
        pass

    def shareToWx(self):
        pass

    def fadeIn(self, sPos, ePos):
        # 进入动画
        self.fadeAnimation.stop()
        self.fadeAnimation.setStartValue(sPos)
        self.fadeAnimation.setEndValue(ePos)
        self.fadeAnimation.start()

    def exec_(self):
        size = self.sizeHint()
        sPos = QCursor.pos()  # 鼠标位置
        sPos.setX(int(sPos.x() - size.width() / 2))
        sPos.setY(sPos.y() - size.height() - 25)
        # 25 是状态栏高度
        ePos = QPoint(sPos.x(), sPos.y() - 25)
        self.fadeIn(sPos, ePos)
        super(ShareMenu, self).exec_(ePos)
