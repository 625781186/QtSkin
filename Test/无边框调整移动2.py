#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton
import win32gui
import win32con


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


class FramelessWindow(QWidget):

    Border = 4
    L, T, R, B, LT, RT, LB, RB = range(1, 9)  # 8个方向

    def __init__(self, *args, **kwargs):
        super(FramelessWindow, self).__init__(*args, **kwargs)
        self.prePos = None
        # 跟踪鼠标
        self.setMouseTracking(True)
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 无边框,任务栏菜单,点击任务栏最小化和还原
        self.setWindowFlags(Qt.FramelessWindowHint)
#         self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint |
#                             Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint)
        # 背景透明窗口的布局（嵌入一个有背景的widget）
        layout = QVBoxLayout(self, spacing=0)
        # 设置边距为2用于判断鼠标的形状和调整窗口大小
        layout.setContentsMargins(
            self.Border, self.Border, self.Border, self.Border)
        # 被内嵌的widget用于包含用户的界面
        self._widget = QWidget(self)
        # 显示背景色
        self._widget.setAutoFillBackground(True)
        # 穿透鼠标事件
        self._widget.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        layout.addWidget(self._widget)
        self._layout = QVBoxLayout(self._widget, spacing=0)
        self._layout.setContentsMargins(0, 0, 0, 0)
        
        style = win32gui.GetWindowLong(int(self.winId()), win32con.GWL_STYLE)
        win32gui.SetWindowLong(int(self.winId()), win32con.GWL_STYLE,style|win32con.WS_THICKFRAME)

    def setWidget(self, widget):
        # 添加包含的用户界面
        self._layout.addWidget(widget)

    def paintEvent(self, event):
        # 画一条带透明度的边框线
        super(FramelessWindow, self).paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(255, 255, 255, 20), self.Border * 2))
        painter.drawRect(self.rect())

    def mousePressEvent(self, event):
        super(FramelessWindow, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.prePos = event.pos()

    def mouseReleaseEvent(self, event):
        super(FramelessWindow, self).mouseReleaseEvent(event)
        self.prePos = None

    def mouseMoveEvent(self, event):
        super(FramelessWindow, self).mouseMoveEvent(event)
        if not self.prePos:
            # 改变鼠标样式
            self.changeCursor(event.pos())
            return
        if self.isMaximized():
            # 禁止拖动
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


class UiWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(UiWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(QPushButton('QLabel', self))


class Window(FramelessWindow):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setWidget(UiWidget(self))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
