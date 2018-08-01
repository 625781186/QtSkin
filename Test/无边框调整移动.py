#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor, QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QRubberBand,\
    QLabel, QApplication, QPushButton


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
        self.isPreview = False  # 预览
        # 屏幕大小
        self.ascreenRect = QApplication.instance().desktop().availableGeometry(self)
        self.screenRect = QApplication.instance().desktop().screenGeometry(self)
        # 跟踪鼠标
        self.setMouseTracking(True)
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 无边框,任务栏菜单,点击任务栏最小化和还原
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint |
                            Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint)
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
        # 橡皮筋（用于拖动调整大小预览）
        self.alphaRubberBand = AlphaRubberBand(QRubberBand.Rectangle)

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
            self.direction = self.changeCursor(event.pos())
            if self.direction:
                self.alphaRubberBand.setGeometry(self.geometry())
                self.alphaRubberBand.show()
                return  # 不是移动是调整大小

    def mouseReleaseEvent(self, event):
        super(FramelessWindow, self).mouseReleaseEvent(event)
        self.prePos = None
        self.alphaRubberBand.close()
        if self.isPreview:
            # 取消预览状态并且设置窗口大小为预览的大小
            self.isPreview = False
            rect = self.alphaRubberBand.geometry()
            if rect.topLeft() == self.ascreenRect.topLeft() and rect.bottomRight() == self.ascreenRect.bottomRight():
                # 最大化
                self.showMaximized()
            else:
                self.setGeometry(rect)

    def mouseMoveEvent(self, event):
        super(FramelessWindow, self).mouseMoveEvent(event)
        if self.alphaRubberBand.isVisible() and not self.isPreview:
            # 改变橡皮筋窗口大小
            print(event.pos() - self.prePos, self.direction)
            return
        if not self.prePos:
            # 改变鼠标样式
            self.changeCursor(event.pos())
            return
        if self.isMaximized():
            # 禁止拖动
            return
        pos = event.pos() - self.prePos
        self.move(self.x() + pos.x(), self.y() + pos.y())

        # 鼠标位置
        mpos = QCursor.pos()
        print(mpos, self.screenRect)
        self.isPreview = True
        if mpos.isNull():
            print('左上角')
        elif mpos.x() == self.screenRect.width() - 1 and mpos.y() == self.screenRect.height() - 1:
            print('右下角')
        elif mpos.x() == 0 and mpos.y() == self.screenRect.height() - 1:
            print('左下角')
        elif mpos.x() == 0:
            # 左边
            self.alphaRubberBand.setGeometry(
                0, 0, int(self.ascreenRect.width() / 2), self.ascreenRect.height())
            self.alphaRubberBand.show()
        elif mpos.x() == self.screenRect.width() - 1:
            # 右边
            self.alphaRubberBand.setGeometry(
                int(self.ascreenRect.width() / 2), 0,
                int(self.ascreenRect.width() / 2), self.ascreenRect.height())
            self.alphaRubberBand.show()
        elif mpos.y() == 0:
            # 上边
            self.alphaRubberBand.setGeometry(self.ascreenRect)
            self.alphaRubberBand.show()
        else:
            self.isPreview = False
            self.alphaRubberBand.setGeometry(self.rect())
            self.alphaRubberBand.close()

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
