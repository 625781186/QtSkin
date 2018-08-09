#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年7月16日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.TitleWidget
@description: 
"""

from PyQt5.QtCore import pyqtSignal, QPoint, Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget

from UiFiles.Ui_TitleWidget import Ui_TitleWidget
from Widgets.Dialogs.LoginDialog import LoginDialog


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"


class TitleWidget(QWidget, Ui_TitleWidget):

    windowMoved = pyqtSignal(QPoint)
    doubleClicked = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(TitleWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.prePos = None

    @pyqtSlot()
    def on_buttonLogin_clicked(self):
        # 登录按钮
        dialog = LoginDialog(self)
        dialog.exec_()

    def mouseDoubleClickEvent(self, event):
        super(TitleWidget, self).mouseDoubleClickEvent(event)
        self.doubleClicked.emit()

    def mousePressEvent(self, event):
        super(TitleWidget, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.prePos = event.pos()

    def mouseReleaseEvent(self, event):
        super(TitleWidget, self).mouseReleaseEvent(event)
        self.prePos = None

    def mouseMoveEvent(self, event):
        super(TitleWidget, self).mouseMoveEvent(event)
        if not self.prePos:
            return
        pos = event.pos() - self.prePos
        self.windowMoved.emit(pos)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from Utils.Tools import readData
    app = QApplication(sys.argv)
    app.setStyleSheet(readData('../Resources/Themes/Default.qss'))
    w = TitleWidget()
    w.show()
    w.windowMoved.connect(lambda pos: w.move(w.x() + pos.x(), w.y() + pos.y()))
    sys.exit(app.exec_())
