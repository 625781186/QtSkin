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
from datetime import datetime
import webbrowser

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QButtonGroup

from Core.SortFilterProxyModel import SortFilterProxyModel
from UiFiles.Ui_MainWindow import Ui_MainWindow
from Widgets.Items.ProjectItemWidget import ProjectItemWidget
from Widgets.ShareMenu import ShareMenu
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

        self.initTitleBar()
        self.initProjects()
        self.initStatusbar()

    @pyqtSlot()
    def on_buttonAddProject_clicked(self):
        """添加项目"""
        name = 'name-'
        time = datetime.now().strftime('%Y/%m/%d')
        item = QStandardItem(name + time)
        self.projectModel.appendRow(item)
        index = self.filterProjectModel.mapFromSource(item.index())
        widget = ProjectItemWidget(self.listViewProjects)
        widget.setName(name)
        widget.setTime(time)
        item.setSizeHint(widget.size())
        self.listViewProjects.setIndexWidget(index, widget)

    def initTitleBar(self):
        # 在菜单中添加自定义的标题栏
        layout = QHBoxLayout(self.menubar, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = TitleWidget(self)
        self.titleWidget.doubleClicked.connect(self.doNormalOrMaxed)
        self.titleWidget.windowMoved.connect(self.doMoveWindow)
        layout.addWidget(self.titleWidget)

    def initProjects(self):
        # 设置listViewProjects的代理滚动
        self.listViewProjects.setVerticalScrollBar(self.rightScrollBar)
        # 由于重新设置了列表的滚动条会被嵌入到QListWidget中,这里需要重新添加到布局中
        self.horizontalLayout.addWidget(self.rightScrollBar)
        self.listViewProjects.setSpacing(15)
        # 两个排序按钮放入一个组中
        btnGroup = QButtonGroup(self)
        btnGroup.addButton(self.buttonSortTime)
        btnGroup.addButton(self.buttonSortAz)
        # 数据模型
        self.projectModel = QStandardItemModel(self.listViewProjects)
        # 排序模型
        self.filterProjectModel = SortFilterProxyModel(self.listViewProjects)
        self.filterProjectModel.setSourceModel(self.projectModel)
        self.listViewProjects.setModel(self.filterProjectModel)

    def initStatusbar(self):
        # 底部状态栏
        self.statusbar.addPermanentWidget(  # 主页按钮
            QPushButton('', self, objectName='buttonHome',
                        statusTip=self.tr('visit home page'),
                        clicked=self.doVisitHome))
        # 分享按钮
        self.buttonShare = QPushButton(
            '', self, objectName='buttonShare',
            statusTip=self.tr('share QtSkin to friends'))
        self.statusbar.addPermanentWidget(self.buttonShare)
        # 分享菜单
        self.shareMenu = ShareMenu(self.tr('Share'), self.buttonShare)
        self.buttonShare.clicked.connect(self.shareMenu.exec_)

    def doVisitHome(self):
        # 访问主页
        webbrowser.open_new_tab('https://github.com/892768447/QtSkin')

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
    sys.exit(app.exec_())
