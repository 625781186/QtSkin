#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年8月16日@
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.DesignerWidget
@description: 
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from UiFiles.Ui_DesignerWidget import Ui_DesignerWidget
from Utils import Constant


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class DesignerWidget(QWidget, Ui_DesignerWidget):

    def __init__(self, *args, **kwargs):
        super(DesignerWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)


if __name__ == '__main__':
    import sys
    import os
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
    w = DesignerWidget()
    w.show()
    sys.exit(app.exec_())
