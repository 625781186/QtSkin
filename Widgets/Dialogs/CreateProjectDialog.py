#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog

from UiFiles.Ui_CreateProjectDialog import Ui_CreateProjectDialog
from Utils import Constant
from Widgets.Dialogs.Dialog import Dialog


# Created on 2018年8月5日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Widgets.Dialogs.CreateProjectDialog
# description:
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class CreateProjectDialog(QDialog, Ui_CreateProjectDialog, Dialog):

    Icon = ''  # 叹号字

    def __init__(self, *args, **kwargs):
        super(CreateProjectDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.dialogWidgetBg.setContentsMargins(1, 1, 1, 1)
        self.BorderWidget = self.dialogWidgetBg  # 边框闪烁
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.widgetTitle.windowMoved.connect(self.doMoveWindow)
        self.widgetTitle.windowClosed.connect(self.reject)

    @pyqtSlot()
    def on_buttonCreate_clicked(self):
        # 创建项目按钮
        name = self.projectName
        if not name:
            self.showErrorMsg(self.tr('Incorrect project name'))
            return
        # 判断项目是否存在
        self.labelNotice.setText('')

    @property
    def projectName(self):
        return self.editProjectName.text().strip()

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
    Constant.BaseDir = '../../'
    app = QApplication(sys.argv)
    app.setStyleSheet(readData('../../Resources/Themes/Default.qss'))
    QFontDatabase.addApplicationFont('../../Resources/Fonts/qtskin.ttf')
    ww = QWidget()
    ww.show()
    w = CreateProjectDialog(ww)
    w.exec_()
    sys.exit(app.exec_())
