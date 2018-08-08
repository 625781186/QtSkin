# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\QtSkin\UiFiles\ProjectItemWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProjectItemWidget(object):
    def setupUi(self, ProjectItemWidget):
        ProjectItemWidget.setObjectName("ProjectItemWidget")
        ProjectItemWidget.resize(240, 210)
        ProjectItemWidget.setMinimumSize(QtCore.QSize(240, 210))
        ProjectItemWidget.setMaximumSize(QtCore.QSize(240, 210))
        ProjectItemWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout = QtWidgets.QVBoxLayout(ProjectItemWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widgetTool = QtWidgets.QWidget(ProjectItemWidget)
        self.widgetTool.setMinimumSize(QtCore.QSize(0, 40))
        self.widgetTool.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widgetTool.setObjectName("widgetTool")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetTool)
        self.horizontalLayout_3.setContentsMargins(0, 5, 5, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.buttonDelete = QtWidgets.QPushButton(self.widgetTool)
        self.buttonDelete.setMinimumSize(QtCore.QSize(30, 30))
        self.buttonDelete.setMaximumSize(QtCore.QSize(30, 30))
        self.buttonDelete.setObjectName("buttonDelete")
        self.horizontalLayout_3.addWidget(self.buttonDelete)
        self.horizontalLayout.addWidget(self.widgetTool)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.widgetBottom = QtWidgets.QWidget(ProjectItemWidget)
        self.widgetBottom.setMinimumSize(QtCore.QSize(0, 50))
        self.widgetBottom.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widgetBottom.setObjectName("widgetBottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetBottom)
        self.horizontalLayout_2.setContentsMargins(20, 18, 20, 18)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelName = QtWidgets.QLabel(self.widgetBottom)
        self.labelName.setText("")
        self.labelName.setObjectName("labelName")
        self.horizontalLayout_2.addWidget(self.labelName)
        self.labelTime = QtWidgets.QLabel(self.widgetBottom)
        self.labelTime.setText("")
        self.labelTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTime.setObjectName("labelTime")
        self.horizontalLayout_2.addWidget(self.labelTime)
        self.horizontalLayout.addWidget(self.widgetBottom)

        self.retranslateUi(ProjectItemWidget)
        QtCore.QMetaObject.connectSlotsByName(ProjectItemWidget)

    def retranslateUi(self, ProjectItemWidget):
        _translate = QtCore.QCoreApplication.translate
        ProjectItemWidget.setWindowTitle(_translate("ProjectItemWidget", "ProjectItemWidget"))
        ProjectItemWidget.setText(_translate("ProjectItemWidget", ""))
        self.buttonDelete.setText(_translate("ProjectItemWidget", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProjectItemWidget = QtWidgets.QLabel()
    ui = Ui_ProjectItemWidget()
    ui.setupUi(ProjectItemWidget)
    ProjectItemWidget.show()
    sys.exit(app.exec_())

