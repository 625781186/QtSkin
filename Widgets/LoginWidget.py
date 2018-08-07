#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog

from Core.Dialog import Dialog
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


class LoginWidget(QDialog, Ui_LoginWidget, Dialog):

    Icon = ''  # 叹号字

    def __init__(self, *args, **kwargs):
        super(LoginWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.loginWidgetBg.setContentsMargins(1, 1, 1, 1)
        self.BorderWidget = self.loginWidgetBg  # 边框闪烁
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.widgetTitle.windowMoved.connect(self.doMoveWindow)
        self.widgetTitle.windowClosed.connect(self.reject)

    @pyqtSlot()
    def on_buttonLogin_clicked(self):
        # 登录点击
        username = self.editUsername.text().strip()
        password = self.editPassword.text().strip()
        if not username and not password:
            self.showErrorMsg(self.tr('Incorrect username or password'))
            return
        if not username:
            self.showErrorMsg(self.tr('Incorrect username'))
            return
        if not password:
            self.showErrorMsg(self.tr('Incorrect password'))
            return
        self.labelNotice.setText('')

    def showErrorMsg(self, msg):
        """
        :param msg: 消息内容
        """
        self.labelNotice.setText(self.Icon + ' ' + msg)


if __name__ == '__main__':
    import sys
    import cgitb
    sys.excepthook = cgitb.Hook(1, None, 5, sys.stderr, 'text')
    from PyQt5.QtWidgets import QApplication, QWidget
    from PyQt5.QtGui import QFontDatabase
    from Utils.Tools import readData
    app = QApplication(sys.argv)
    app.setStyleSheet(readData('../Resources/Themes/Default.qss'))
    QFontDatabase.addApplicationFont('../Resources/Fonts/qtskin.ttf')
    ww = QWidget()
    ww.show()
    w = LoginWidget(ww)
    w.exec_()
    sys.exit(app.exec_())
