# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\QtSkin\UiFiles\CreateProjectDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateProjectDialog(object):
    def setupUi(self, CreateProjectDialog):
        CreateProjectDialog.setObjectName("CreateProjectDialog")
        CreateProjectDialog.resize(320, 210)
        self.horizontalLayout = QtWidgets.QHBoxLayout(CreateProjectDialog)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dialogWidgetBg = QtWidgets.QWidget(CreateProjectDialog)
        self.dialogWidgetBg.setMinimumSize(QtCore.QSize(310, 200))
        self.dialogWidgetBg.setMaximumSize(QtCore.QSize(310, 200))
        self.dialogWidgetBg.setProperty("active", True)
        self.dialogWidgetBg.setObjectName("dialogWidgetBg")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dialogWidgetBg)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widgetTitle = BaseTitleWidget(self.dialogWidgetBg)
        self.widgetTitle.setMaximumSize(QtCore.QSize(16777215, 28))
        self.widgetTitle.setObjectName("widgetTitle")
        self.verticalLayout_2.addWidget(self.widgetTitle)
        self.widgetEdit = QtWidgets.QWidget(self.dialogWidgetBg)
        self.widgetEdit.setObjectName("widgetEdit")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetEdit)
        self.verticalLayout.setContentsMargins(25, 32, 25, 32)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editProjectName = QtWidgets.QLineEdit(self.widgetEdit)
        self.editProjectName.setMinimumSize(QtCore.QSize(0, 30))
        self.editProjectName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.editProjectName.setClearButtonEnabled(True)
        self.editProjectName.setObjectName("editProjectName")
        self.verticalLayout.addWidget(self.editProjectName)
        self.labelNotice = QtWidgets.QLabel(self.widgetEdit)
        self.labelNotice.setText("")
        self.labelNotice.setObjectName("labelNotice")
        self.verticalLayout.addWidget(self.labelNotice)
        self.buttonCreate = QtWidgets.QPushButton(self.widgetEdit)
        self.buttonCreate.setMinimumSize(QtCore.QSize(0, 36))
        self.buttonCreate.setMaximumSize(QtCore.QSize(16777215, 36))
        self.buttonCreate.setDefault(True)
        self.buttonCreate.setObjectName("buttonCreate")
        self.verticalLayout.addWidget(self.buttonCreate)
        self.verticalLayout_2.addWidget(self.widgetEdit)
        self.horizontalLayout.addWidget(self.dialogWidgetBg)

        self.retranslateUi(CreateProjectDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateProjectDialog)

    def retranslateUi(self, CreateProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        CreateProjectDialog.setWindowTitle(_translate("CreateProjectDialog", "Create Project"))
        self.editProjectName.setPlaceholderText(_translate("CreateProjectDialog", "项目名称"))
        self.buttonCreate.setText(_translate("CreateProjectDialog", "创建项目"))

from Widgets.BaseTitleWidget import BaseTitleWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateProjectDialog = QtWidgets.QDialog()
    ui = Ui_CreateProjectDialog()
    ui.setupUi(CreateProjectDialog)
    CreateProjectDialog.show()
    sys.exit(app.exec_())

