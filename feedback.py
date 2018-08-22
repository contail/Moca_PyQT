# -*- coding: utf-8 -*-
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt


class Form(QWidget):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi()

        #button hooks
        self.pb.clicked.connect(lambda : self.get_file_name())

    def setupUi(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.resize(480, 320)
        self.setWindowTitle("피드백")

        box = QBoxLayout(QBoxLayout.TopToBottom)
        self.lb = QLabel()
        self.lb_1 = QLabel()

        self.pb = QPushButton("이미지 파일을 선택해주세요",self)
        box.addWidget(self.lb)
        box.addWidget(self.pb)
        self.setLayout(box)
        box.addWidget(self.lb_1)


    def start_feedback(self):
        return 1


    def get_file_name(self):

        filename = QFileDialog.getOpenFileName()
        self.lb.setText(filename[0])
        pixmap = QPixmap(filename[0])
        pixmap = pixmap.scaledToHeight(240)
        self.lb_1.setPixmap(pixmap)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())