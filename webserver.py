# -*- coding: utf-8 -*-
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal, QThread

from PyQt5 import QtCore, QtWidgets
import subprocess



class Form(QWidget):



    def __init__(self):
        super(self.__class__, self).__init__()
        server_info = self.get_ip_info() + ":" + self.get_port_info() + "/admin 으로 \n 접속해주세요!"
        self.setupUi(server_info)

        #hooks button
        self.OK_button.clicked.connect(lambda: self.ok_button(server_info))

    def setupUi(self,server_info):
        QWidget.__init__(self, flags=Qt.Widget)

        self.setWindowTitle("웹서버 정보")
        self.resize(480, 320)
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")


        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(100, 100, 271, 80))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText(server_info)

        self.OK_button = QtWidgets.QPushButton(self.centralWidget)
        self.OK_button.setGeometry(QtCore.QRect(180, 200, 120, 80))
        self.OK_button.setObjectName("buttonBox")
        self.OK_button.setText("확인")


    def ok_button(self, server_info):
        # subprocess.call("python manage.py runserver "+server_info,shell=True)
        subprocess.call("python main.py", shell=True)
        self.close()


    def get_ip_info(self):
        r = open('mocaUtils/ipAddress.txt', mode='rt', encoding='utf-8')
        return r.readline()
    def get_port_info(self):
        r = open('mocaUtils/port.txt', mode='rt', encoding='utf-8')
        return r.readline()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())