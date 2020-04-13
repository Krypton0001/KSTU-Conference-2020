# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.image = QtWidgets.QWidget(self.tab)
        self.image.setObjectName("image")
        self.horizontalLayout_3.addWidget(self.image)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_cancel = QtWidgets.QPushButton(self.tab)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.btn_ok = QtWidgets.QPushButton(self.tab)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_2.addWidget(self.btn_ok)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.camera = QtWidgets.QWidget(self.tab_2)
        self.camera.setObjectName("camera")
        self.horizontalLayout_5.addWidget(self.camera)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_cam = QtWidgets.QPushButton(self.tab_2)
        self.btn_cam.setObjectName("btn_cam")
        self.horizontalLayout_4.addWidget(self.btn_cam)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_close = QtWidgets.QPushButton(Dialog)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_cancel.setText(_translate("Dialog", "Cancel"))
        self.btn_ok.setText(_translate("Dialog", "Ok"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Image"))
        self.btn_cam.setText(_translate("Dialog", "Run camera"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Camera"))
        self.btn_close.setText(_translate("Dialog", "Close"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())