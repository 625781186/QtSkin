#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年7月16日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.Mainwindow
@description: 
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout

from UiFiles.Ui_MainWindow import Ui_MainWindow
from Widgets.TitleWidget import TitleWidget


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"


class Mainwindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(Mainwindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # 在菜单中添加自定义的标题栏
        layout = QHBoxLayout(self.menubar, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = TitleWidget(self)
        self.titleWidget.doubleClicked.connect(self.doNormalOrMaxed)
        self.titleWidget.windowMoved.connect(self.doMoveWindow)
        layout.addWidget(self.titleWidget)
        
        #设置listWidgetProjects的代理滚动
        self.listWidgetProjects.setVerticalScrollBar(self.rightScrollBar)
        #由于重新设置了列表的滚动条会被嵌入到QListWidget中,这里需要重新添加到布局中
        self.horizontalLayout.addWidget(self.rightScrollBar)

    def doMoveWindow(self, pos):
        if self.isMaximized() or self.isFullScreen():
            return
        # 移动窗口
        self.move(self.x() + pos.x(), self.y() + pos.y())

    def doNormalOrMaxed(self):
        # 还原或者最大化
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QFontDatabase
    from Utils.Tools import readData
    app = QApplication(sys.argv)
    app.setStyleSheet(readData('../Resources/Themes/Default.qss'))
    QFontDatabase.addApplicationFont('../Resources/qtskin.ttf')
    w = Mainwindow()
    w.show()
    w.progressBar.setValue(50)
    w.listWidgetProjects.addItems([str(i) for i in range(1000)])
    sys.exit(app.exec_())
