#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget

from UiFiles.Ui_LoginWidget import Ui_LoginWidget


# Created on 2018年8月5日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Widgets.LoginWidget
# description:
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class LoginWidget(QWidget, Ui_LoginWidget):

    def __init__(self, *args, **kwargs):
        super(LoginWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.widgetTitle.windowMoved.connect(self.doMoveWindow)

    def doMoveWindow(self, pos):
        if self.isMaximized() or self.isFullScreen():
            return
        # 移动窗口
        self.move(self.x() + pos.x(), self.y() + pos.y())


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from Utils.Tools import readData
    app = QApplication(sys.argv)
    app.setStyleSheet(readData('../Resources/Themes/Default.qss'))
    w = LoginWidget()
    w.show()
    sys.exit(app.exec_())
