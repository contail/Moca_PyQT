# -*- coding: utf-8 -*-
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt

from PyQt5 import QtCore, QtWidgets


class Form(QWidget):

    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)

        self.setWindowTitle("웹서버 정보")
        self.resize(480,320)
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        server_info = self.get_ip_info() + ":" +self.get_port_info()+"/admin 으로 \n 접속해주세요!"

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(100, 100, 271, 80))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText(server_info)

        self.OK_button = QtWidgets.QPushButton(self.centralWidget)
        self.OK_button.setGeometry(QtCore.QRect(180, 200, 120, 80))
        self.OK_button.setObjectName("buttonBox")
        self.OK_button.setText("확인")
        self.OK_button.clicked.connect(self.close)


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