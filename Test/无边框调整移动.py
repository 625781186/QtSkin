#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QRubberBand,\
    QLabel


# Created on 2018年7月31日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Test.无边框调整移动
# description:
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class AlphaRubberBand(QRubberBand):
    pass


class FramelessWindow(QWidget):

    Border = 4
    L, T, R, B, LT, RT, LB, RB = range(1, 9)  # 8个方向

    def __init__(self, *args, **kwargs):
        super(FramelessWindow, self).__init__(*args, **kwargs)
        self.prePos = None
        self.direction = 0  # 方向
        self.setMouseTracking(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint |
                            Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint)
        # 橡皮筋
        self.alphaRubberBand = AlphaRubberBand(QRubberBand.Rectangle)

    def paintEvent(self, event):
        # 画一条带透明度的边框线
        super(FramelessWindow, self).paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(255, 255, 255, 50), self.Border))
        painter.drawRect(self.rect())

    def mousePressEvent(self, event):
        super(FramelessWindow, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.prePos = event.pos()
            self.direction = self.changeCursor(event.pos())
            if self.direction:
                self.alphaRubberBand.setGeometry(self.geometry())
                self.alphaRubberBand.show()
                return  # 不是移动是调整大小

    def mouseReleaseEvent(self, event):
        super(FramelessWindow, self).mouseReleaseEvent(event)
        self.prePos = None
        self.alphaRubberBand.close()

    def mouseMoveEvent(self, event):
        super(FramelessWindow, self).mouseMoveEvent(event)
        if self.alphaRubberBand.isVisible():
            # 改变橡皮筋窗口大小
            print(event.pos() - self.prePos, self.direction)
            return
        if not self.prePos:
            # 改变鼠标样式
            self.changeCursor(event.pos())
            return
        pos = event.pos() - self.prePos
        self.move(self.x() + pos.x(), self.y() + pos.y())

    def changeCursor(self, pos):
        x, y, w, h = pos.x(), pos.y(), self.width(), self.height()
        lx = x < self.Border
        rx = x > w - self.Border
        ty = y < self.Border
        by = y > h - self.Border
        # 左上角
        if (lx and ty):
            self.setCursor(Qt.SizeFDiagCursor)
            return self.LT
        # 右下角
        if (rx and by):
            self.setCursor(Qt.SizeFDiagCursor)
            return self.RB
        # 右上角
        if (rx and ty):
            self.setCursor(Qt.SizeBDiagCursor)
            return self.RT
        # 左下角
        if (lx and by):
            self.setCursor(Qt.SizeBDiagCursor)
            return self.LB
        # 上
        if ty:
            self.setCursor(Qt.SizeVerCursor)
            return self.T
        # 下
        if by:
            self.setCursor(Qt.SizeVerCursor)
            return self.B
        # 左
        if lx:
            self.setCursor(Qt.SizeHorCursor)
            return self.L
        # 右
        if rx:
            self.setCursor(Qt.SizeHorCursor)
            return self.R
        self.setCursor(Qt.ArrowCursor)
        return 0


class Window(FramelessWindow):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(
            self.Border, self.Border, self.Border, self.Border)
        layout.addWidget(QLabel('QLabel', self))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
