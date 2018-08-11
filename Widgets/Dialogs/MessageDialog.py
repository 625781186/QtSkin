#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年8月11日@
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.Dialogs.MessageDialog
@description: 消息对话框
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from UiFiles.Ui_MessageDialog import Ui_MessageDialog
from Widgets.Dialogs.Dialog import Dialog


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class MessageDialog(QDialog, Ui_MessageDialog, Dialog):

    def __init__(self, *args, title='', message='', **kwargs):
        super(MessageDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.dialogWidgetBg.setContentsMargins(1, 1, 1, 1)
        self.BorderWidget = self.dialogWidgetBg  # 边框闪烁
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.widgetTitle.windowMoved.connect(self.doMoveWindow)
        self.widgetTitle.windowClosed.connect(self.reject)
        self.setTitle(title).setMessage(message)

    def showCancelButton(self, show=True):
        """设置取消按钮是否可见
        :param show: True or False
        """
        self.buttonCancel.setVisible(show)

    def setTitle(self, title):
        """设置标题文字
        :param title: 标题
        """
        self.widgetTitle.setTitle(title)
        return self

    def setMessage(self, message):
        """设置提示消息
        :param message: 提示消息
        """
        self.labelMessage.setText(message)
        return self

    def close(self):
        super(MessageDialog, self).close()
        self.deleteLater()

    @classmethod
    def information(cls, parent=None, title='', message=''):
        """消息提示框
        :param cls:
        :param title: 标题
        :param message: 内容
        """
        dialog = MessageDialog(parent, title=title, message=message)
        dialog.showCancelButton(False)
        ret = dialog.exec_()
        dialog.close()
        return ret

    @classmethod
    def error(cls, parent=None, title='', message=''):
        """错误提示框
        :param cls:
        :param title: 标题
        :param message: 内容
        """
        dialog = MessageDialog(parent, title=title, message=message)
        dialog.setProperty('active', 'error')
        dialog.showCancelButton(False)
        ret = dialog.exec_()
        dialog.close()
        return ret

    @classmethod
    def question(cls, parent=None, title='', message=''):
        """询问提示框
        :param cls:
        :param title: 标题
        :param message: 内容
        """
        dialog = MessageDialog(parent, title=title, message=message)
        ret = dialog.exec_()
        dialog.close()
        return ret


if __name__ == '__main__':
    import sys
    import cgitb
    sys.excepthook = cgitb.Hook(1, None, 5, sys.stderr, 'text')
    from PyQt5.QtWidgets import QApplication, QWidget
    from PyQt5.QtGui import QFontDatabase
    from Utils.Tools import readData
    app = QApplication(sys.argv)
    app.setStyleSheet(readData('../../Resources/Themes/Default.qss'))
    QFontDatabase.addApplicationFont('../../Resources/Fonts/qtskin.ttf')
    ww = QWidget()
    ww.show()
    w = MessageDialog(ww, title='删除xxxx?', message='删除xx后无法恢复。')
    w.exec_()
    MessageDialog.information(ww, '删除xxxx?', '删除xx后无法恢复。')
    MessageDialog.question(ww, '删除xxxx?', '删除xx后无法恢复。')
    MessageDialog.error(ww, '删除xxxx?', '删除xx后无法恢复。')
    sys.exit(app.exec_())
