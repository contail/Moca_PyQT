# -*- coding: utf-8 -*-
# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html
# by James Lewis (@baldengineer)
# Minimal python code to start PyQt5 GUI
#

# always seem to need this
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *

# This is our window from QtCreator
import mainwindow_auto
import subprocess
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call



    def pressedCameraButton(self):
        print ("Pressed On!")
        #python camera.py로 하나 만들기
        subprocess.call('python main.py', shell=True, )
    def pressedWebStoreButton(self):
        print ("Pressed Off!")
    def pressedFeedbackButton(self):
        subprocess.call('python feedback.py', shell=True, )
    def pressedFSettingsButton(self):
        print("pressedFSettingsButton")

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        ### Hooks to for buttons
        self.btn1.clicked.connect(lambda: self.pressedCameraButton())
        self.btn2.clicked.connect(lambda: self.pressedWebStoreButton())
        self.btn3.clicked.connect(lambda: self.pressedFeedbackButton())
        self.btn4.clicked.connect(lambda: self.pressedFSettingsButton())



# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()