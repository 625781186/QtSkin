# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Workspace\QtSkin\UiFiles\LoginWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        LoginWidget.setObjectName("LoginWidget")
        LoginWidget.resize(402, 566)
        LoginWidget.setMinimumSize(QtCore.QSize(0, 430))
        self.gridLayout = QtWidgets.QGridLayout(LoginWidget)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(LoginWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addWidget(self.widget, 4, 0, 1, 3)
        self.widgetTitle = BaseTitleWidget(LoginWidget)
        self.widgetTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widgetTitle.setObjectName("widgetTitle")
        self.gridLayout.addWidget(self.widgetTitle, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(LoginWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(LoginWidget)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(LoginWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 1)

        self.retranslateUi(LoginWidget)
        QtCore.QMetaObject.connectSlotsByName(LoginWidget)

    def retranslateUi(self, LoginWidget):
        _translate = QtCore.QCoreApplication.translate
        LoginWidget.setWindowTitle(_translate("LoginWidget", "Login"))
        self.pushButton.setText(_translate("LoginWidget", "PushButton"))
        self.label_3.setText(_translate("LoginWidget", "<html><head/><body><p><a href=\"https://github.com/password_reset\"><span style=\" text-decoration: none; color:rgb(93, 94, 94);\">忘记密码?</span></a></p></body></html>"))
        self.label_2.setText(_translate("LoginWidget", "<html><head/><body><p><a href=\"https://github.com/join?source=login\"><span style=\" text-decoration: none; color:#0000ff;\">立即注册</span></a></p></body></html>"))
        self.label.setText(_translate("LoginWidget", "头像"))

from Widgets.BaseTitleWidget import BaseTitleWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWidget = QtWidgets.QWidget()
    ui = Ui_LoginWidget()
    ui.setupUi(LoginWidget)
    LoginWidget.show()
    sys.exit(app.exec_())

