import sys
from detectgui import *
from detect_face_image import *
from detect_face_video import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit
 
from PyQt5.QtGui import QPixmap 
#img = cv2.imread('ten.jpg')
# Create application
app = QtWidgets.QApplication(sys.argv)

# Created for open interface in the window
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def btnPressClose():
    sys.exit(app.exec_())
    pass



# Build logic path for the detect face from image
class DetectImg:
    def btnPressCls(self):
        ui.plainTextEdit.appendPlainText("Clear")
        ui.plainTextEdit.clear()
        print("Clicked button Cancel !!!")
        pass

    def onActivated(text):
        textImg = tsoi
        ui.plainTextEdit.appendPlainText(textImg)
    
    def btnPressRun(self):
        #d = cv2.imshow("Img", img)
        if ui.rbImg.isChecked():
            ui.plainTextEdit.appendPlainText("Runed detect face from img")
            d = cv2.imshow("Img", img)
            ui.plainTextEdit.appendPlainText(d)
            pass
        elif ui.rbCam.isChecked():
            ui.plainTextEdit.appendPlainText("Runed detect face from computer vision in mode RT")
            cam = DetectFaceCam
            cam.runCam()
            pass
        else:
            ui.plainTextEdit.appendPlainText(textImg)
            ui.plainTextEdit.appendPlainText("Select the rinning function")
            pass
    ui.comboBox.activated[str].connect(onActivated)

# Build logic path for the detect face with Web Cam on the real time
class DetectCam:
    def rbcam(self):
        return True


    

# Create 
dtcImg = DetectImg
dtcCam = DetectCam



ui.plainTextEdit
# Event button clicked from class DetectImg
ui.btnCls.clicked.connect(dtcImg.btnPressCls)
ui.btnRun.clicked.connect(dtcImg.btnPressRun)
ui.btnExt.clicked.connect(btnPressClose)
# Event button run camera
sys.exit(app.exec_())
