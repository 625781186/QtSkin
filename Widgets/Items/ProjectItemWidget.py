#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年8月6日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.Items.ProjectItemWidget
@description: 主页项目Item
"""

import os
import shutil

from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QModelIndex
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QLabel

from UiFiles.Ui_ProjectItemWidget import Ui_ProjectItemWidget
from Utils import Constant
from Utils.Tools import log
from Widgets.Dialogs.MessageDialog import MessageDialog


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"


class ProjectItemWidget(QLabel, Ui_ProjectItemWidget):

    itemDeleted = pyqtSignal(QModelIndex)

    def __init__(self, project, index, *args, **kwargs):
        super(ProjectItemWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # 隐藏删除按钮
        self.buttonDelete.setVisible(False)
        self._project = project
        self._index = index
        self.setName(project['name'])
        self.setTime(project['time'].split('-')[0])

    @property
    def project(self):
        return self._project

    @property
    def index(self):
        return self._index

    @pyqtSlot()
    def on_buttonDelete_clicked(self):
        # 删除项目
        if MessageDialog.question(
            self,
            self.tr('Delete "{}" project?').format(self._project['name']),
            self.tr('Delete operation cannot be resumed.')
        ) != MessageDialog.Accepted:
            return
        try:
            dirPath = os.path.abspath(os.path.join(
                Constant.BaseDir, 'Projects', self._project['name']))
            # 删除项目文件
            os.unlink(dirPath + '.project')
            # 删除目录
            shutil.rmtree(dirPath)
            self.itemDeleted.emit(self._index)
        except Exception as e:
            log.error(str(e))
            MessageDialog.error(self, self.tr('Error'), str(e.args))

    def setName(self, name):
        """
        :param name: 项目名称
        """
        self.labelName.setText(name)
        return self

    def setTime(self, time):
        """
        :param time: 修改时间
        """
        self.labelTime.setText(time)
        return self

    def showEmpty(self, show=True):
        """
        :param show: 显示空项目文字
        """
        self.labelEmpty.setVisible(show)
        return self

    def enterEvent(self, event):
        """鼠标进入时显示删除按钮"""
        super(ProjectItemWidget, self).enterEvent(event)
        self.buttonDelete.setVisible(True)

    def leaveEvent(self, event):
        """鼠标离开时隐藏删除按钮"""
        super(ProjectItemWidget, self).leaveEvent(event)
        self.buttonDelete.setVisible(False)

    def paintEvent(self, event):
        super(ProjectItemWidget, self).paintEvent(event)
        pixmap = self.pixmap()
        if not pixmap or pixmap.isNull():
            # 画虚线边框
            painter = QPainter(self)
            pen = painter.pen()
            pen.setStyle(Qt.DashLine)
            pen.setWidth(2)
            painter.setPen(pen)
            painter.drawRoundedRect(
                self.rect().adjusted(20, 20, -20, -20), 4, 4)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QFontDatabase
    from Utils.Tools import readData
    app = QApplication(sys.argv)
    app.setStyleSheet(readData('../../Resources/Themes/Default.qss'))
    QFontDatabase.addApplicationFont('../../Resources/Fonts/qtskin.ttf')
    w = ProjectItemWidget({'name': 'name', 'time': '2018/8/9'})
    w.show()
    sys.exit(app.exec_())
