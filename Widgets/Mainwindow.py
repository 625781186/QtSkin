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
<<<<<<< HEAD

import os
from pathlib import Path
import webbrowser

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QButtonGroup

from UiFiles.Ui_MainWindow import Ui_MainWindow
from Utils import Constant
from Utils.Project import Project
from Utils.SortFilterProxyModel import SortFilterProxyModel
from Utils.Tools import log
from Widgets.Dialogs.CreateProjectDialog import CreateProjectDialog
from Widgets.Items.ProjectItemWidget import ProjectItemWidget
from Widgets.Menus.ShareMenu import ShareMenu
=======
import webbrowser 
#import sys 
#sys.path.append("...")
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QButtonGroup

from QtSkin.UiFiles.Ui_MainWindow import Ui_MainWindow
from Widgets.ShareMenu import ShareMenu
>>>>>>> ff98375d0bca219749730b0cf5103b78d251efe9
from Widgets.TitleWidget import TitleWidget


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"


class Mainwindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(Mainwindow, self).__init__(*args, **kwargs)
        log.debug('')
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 隐藏进度条
        self.progressBar.setVisible(False)

        self.initTitleBar()
        self.initProjectsUi()
        self.initStatusbar()
        self.initProjects()

    def on_buttonSortTime_toggled(self, toggled):
        # 按时间排序
        if toggled:
            log.debug('sort by time')
            self.filterProjectModel.sort(0, Qt.DescendingOrder)

    def on_buttonSortAz_toggled(self, toggled):
        # 按字母排序
        if toggled:
            log.debug('sort by name')
            self.filterProjectModel.sort(0, Qt.AscendingOrder)

    @pyqtSlot()
    def on_buttonAddProject_clicked(self):
        """添加项目"""
        log.debug('')
        dialog = CreateProjectDialog(self)
        if dialog.exec_() != CreateProjectDialog.Accepted:
            log.debug('cancel create project')
            return
        log.debug('project info: %s' % str(dialog.project))
        item = QStandardItem('{} {}'.format(
            dialog.project.name, dialog.project.time))
        self.projectModel.appendRow(item)
        index = self.filterProjectModel.mapFromSource(item.index())
        widget = ProjectItemWidget(
            dialog.project, item, self.listViewProjects)
        widget.itemDeleted.connect(self.doProjectItemDelete)
        dialog.close()
        item.setSizeHint(widget.size())
        self.listViewProjects.setIndexWidget(index, widget)
        self.listViewProjects.setCurrentIndex(index)  # 默认选中
        # 排序
        self.filterProjectModel.sort(
            0, Qt.AscendingOrder if self.buttonSortAz.isChecked() else Qt.DescendingOrder)
    
    def on_listViewProjects_doubleClicked(self,index):
        print(self.filterProjectModel.mapToSource(index).row())

    def initTitleBar(self):
        log.debug('')
        # 在菜单中添加自定义的标题栏
        layout = QHBoxLayout(self.menubar, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = TitleWidget(self)
        self.titleWidget.doubleClicked.connect(self.doNormalOrMaxed)
        self.titleWidget.windowMoved.connect(self.doMoveWindow)
        layout.addWidget(self.titleWidget)

    def initProjectsUi(self):
        log.debug('')
        # 设置listViewProjects的代理滚动
        self.listViewProjects.setVerticalScrollBar(self.rightScrollBar)
        # 由于重新设置了列表的滚动条会被嵌入到QListWidget中,这里需要重新添加到布局中
        self.horizontalLayout.addWidget(self.rightScrollBar)
        self.listViewProjects.setSpacing(15)  # item之间的间隔
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
        log.debug('')
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

    def initProjects(self):
        # 扫描文件并加载项目列表
        log.debug('load projects')
        files = list(Path(os.path.abspath(os.path.join(
            Constant.BaseDir, 'Projects'))).rglob('*.project'))
        log.debug('files: %s' % files)
        if not files:
            return
        self.progressBar.setVisible(False)
        self.progressBar.setRange(0, len(files))  # 进度条范围
        for i, file in enumerate(files):
            try:
                project = Project(file.name)
                if project.load() != None:  # 加载失败跳过
                    continue
                log.debug('project info: %s' % project)
                item = QStandardItem('{} {}'.format(
                    project.name, project.time))
                self.projectModel.appendRow(item)
                index = self.filterProjectModel.mapFromSource(item.index())
                widget = ProjectItemWidget(
                    project, item, self.listViewProjects)
                widget.itemDeleted.connect(self.doProjectItemDelete)
                item.setSizeHint(widget.size())
                self.listViewProjects.setIndexWidget(index, widget)
                self.listViewProjects.setCurrentIndex(index)  # 默认选中
                # 排序
                self.filterProjectModel.sort(
                    0, Qt.AscendingOrder if self.buttonSortAz.isChecked() else Qt.DescendingOrder)
            except Exception as e:
                log.error('load project {} error: {}'.format(file, e))
            self.progressBar.setValue(i + 1)

        self.progressBar.setVisible(False)
        self.progressBar.setRange(-1, 0)

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

    def doProjectItemDelete(self, item):
        # 删除item
        self.projectModel.removeRow(item.index().row())


if __name__ == '__main__':
    import sys
    import cgitb
    sys.excepthook = cgitb.Hook(1, None, 5, sys.stderr, 'text')
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QFontDatabase
    from Utils.Tools import readData, initLog
    initLog()
    Constant.BaseDir = '..'
    os.makedirs('../Projects', exist_ok=True)
    app = QApplication(sys.argv)
    app.setStyleSheet(readData('../Resources/Themes/Default.qss'))
    QFontDatabase.addApplicationFont('../Resources/Fonts/qtskin.ttf')
    w = Mainwindow()
    w.show()
    w.progressBar.setValue(50)
    sys.exit(app.exec_())
