#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年7月16日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.BaseTitleWidget
@description: 
"""

from PyQt5.QtCore import pyqtSignal, QPoint, Qt
from PyQt5.QtWidgets import QWidget

from UiFiles.Ui_BaseTitleWidget import Ui_BaseTitleWidget


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"


class BaseTitleWidget(QWidget, Ui_BaseTitleWidget):

    windowMoved = pyqtSignal(QPoint)
    windowClosed = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(BaseTitleWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 关闭按钮传递关闭信号
        self.buttonClose.clicked.connect(self.windowClosed.emit)
        self.prePos = None

    def mousePressEvent(self, event):
        super(BaseTitleWidget, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.prePos = event.pos()

    def mouseReleaseEvent(self, event):
        super(BaseTitleWidget, self).mouseReleaseEvent(event)
        self.prePos = None

    def mouseMoveEvent(self, event):
        super(BaseTitleWidget, self).mouseMoveEvent(event)
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
    w = BaseTitleWidget()
    w.show()
    w.windowMoved.connect(lambda pos: w.move(w.x() + pos.x(), w.y() + pos.y()))
    sys.exit(app.exec_())
