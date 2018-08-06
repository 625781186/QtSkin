#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年8月6日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.Items.ProjectItemWidget
@description: 
"""
from PyQt5.QtWidgets import QLabel

from UiFiles.Ui_ProjectItemWidget import Ui_ProjectItemWidget


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"


class ProjectItemWidget(QLabel, Ui_ProjectItemWidget):

    def __init__(self, *args, **kwargs):
        super(ProjectItemWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QFontDatabase
    from Utils.Tools import readData
    app = QApplication(sys.argv)
    app.setStyleSheet(readData('../../Resources/Themes/Default.qss'))
    QFontDatabase.addApplicationFont('../../Resources/qtskin.ttf')
    w = ProjectItemWidget()
    w.show()
    sys.exit(app.exec_())
