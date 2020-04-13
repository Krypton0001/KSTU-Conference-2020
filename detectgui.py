# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detect.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

egypt = 'egypt.jpg'
katkova = 'katkova.jpg'
musina = 'musina.jpg'
ramatov = 'ramatov.jpg'
our = 'our.jpg'
saliev = 'saliev.jpg'
tsoi = 'tsoi.jpg'
ya = 'ya.jpg'

textImg = our

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setMinimumSize(QtCore.QSize(480, 640))
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"    background-color: #999;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbImg = QtWidgets.QRadioButton(self.centralwidget)
        self.rbImg.setStyleSheet("QRadioButton\n"
"{\n"
"    background-color: #222;\n"
"    color: #fff;\n"
"}\n"
"\n"
"")
        self.rbImg.setObjectName("rbImg")
        self.verticalLayout.addWidget(self.rbImg)
        self.rbCam = QtWidgets.QRadioButton(self.centralwidget)
        self.rbCam.setStyleSheet("QRadioButton\n"
"{\n"
"    background-color: #222;\n"
"    color: #fff;\n"
"}\n"
"\n"
"")
        self.rbCam.setObjectName("rbCam")
        self.verticalLayout.addWidget(self.rbCam)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: #222;\n"
"    color: #eb34a2;\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.addItem("Saliev")
        self.comboBox.addItem("Ten")
        self.comboBox.addItem("Tsoi")
        self.comboBox.addItem("Katkova")
        self.comboBox.addItem("Musina")
        self.comboBox.addItem("Ramatov")
        self.comboBox.addItem("Our")
        self.comboBox.addItem("I")
        self.comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    background-color: #222;\n"
"    color: #eb34a2;\n"
"}\n"
"\n"
"QComboBox::hover\n"
"{\n"
"    background-color: #34eb55;\n"
"    color: #000;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit\n"
"{\n"
"    background-color: #212;\n"
"    color: #34eb55;\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCls = QtWidgets.QPushButton(self.centralwidget)
        self.btnCls.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #222;\n"
"    color: #d3d3d3;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #34eb55;\n"
"    color: black;\n"
"}\n"
"\n"
"")
        self.btnCls.setObjectName("btnCls")
        self.horizontalLayout.addWidget(self.btnCls)
        self.btnRun = QtWidgets.QPushButton(self.centralwidget)
        self.btnRun.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #222;\n"
"    color: #d3d3d3;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #34eb55;\n"
"    color: black;\n"
"}\n"
"\n"
"")
        self.btnRun.setObjectName("btnRun")
        self.horizontalLayout.addWidget(self.btnRun)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnExt = QtWidgets.QPushButton(self.centralwidget)
        self.btnExt.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #222;\n"
"    color: #d3d3d3;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #eb34a2;\n"
"    color: black;\n"
"}\n"
"\n"
"")
        self.btnExt.setObjectName("btnExt")
        self.verticalLayout_2.addWidget(self.btnExt)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rbImg.setText(_translate("MainWindow", "Detect from Img"))
        self.rbCam.setText(_translate("MainWindow", "Computer vision RT"))
        self.label.setText(_translate("MainWindow", "Select img"))
        self.btnCls.setText(_translate("MainWindow", "Clear"))
        self.btnRun.setText(_translate("MainWindow", "Let\'s"))
        self.btnExt.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
