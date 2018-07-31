#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import uic
from PyQt5.QtCore import Qt, QEvent, QRect
from PyQt5.QtGui import QMouseEvent, QPainter, QPen
from PyQt5.QtWidgets import QMdiArea, QRubberBand, QLabel, QFrame, QProgressBar


# Created on 2018年7月31日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Test.加载ui描绘边界
# description:
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class RubberBand(QRubberBand):

    def paintEvent(self, _):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 1, Qt.DashLine))
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(self.rect())


class Window(QMdiArea):

    RubberBands = {}

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        widget = uic.loadUi('untitled.ui')
        self.addSubWindow(widget)
        widget.show()
        self.RubberBands[id(widget)] = RubberBand(
            QRubberBand.Rectangle, widget)
        for child in vars(widget).values():
            child.installEventFilter(self)

    def eventFilter(self, obj, event):
        if isinstance(event, QMouseEvent) and hasattr(obj, 'pos') and obj.parent() and event.type() == QEvent.MouseButtonPress:
            widget = obj
            print(obj)
            pos = obj.parent().mapToGlobal(obj.pos())
            while widget.parent():
                widget = widget.parent()
                wid = id(widget)
                if wid in self.RubberBands:
                    pos = widget.mapFromGlobal(pos)
                    band = self.RubberBands[wid]
                    band.setGeometry(QRect(pos, obj.size()))
                    band.show()
                    break
            if isinstance(obj, (QLabel, QFrame,QProgressBar)):
                return True
        return super(Window, self).eventFilter(obj, event)

    def closeEvent(self, event):
        self.closeAllSubWindows()
        super(Window, self).closeEvent(event)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
