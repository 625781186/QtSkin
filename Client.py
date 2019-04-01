#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 2018年8月2日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Client
# description:
import sys

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

from Utils.Tools import readData
from Widgets.Mainwindow import Mainwindow


__Author__ = """By: Irony
QQ: 892768447
Emailfile:/D:/CodePro/Py/0_pyqtPRO____/38_jianyu_smicon/Main.py: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(readData('Resources/Themes/Default.qss'))
    QFontDatabase.addApplicationFont('Resources/Fonts/qtskin.ttf')
    w = Mainwindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
