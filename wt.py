import sys
from PyQt5.QtWidgets import QWidget,QApplication,QFileDialog
# 图片装载的容器
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

from sub import Ui_slaveWidget


class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        mainWidget.setObjectName("mainWidget")
        mainWidget.resize(400, 300)
        self.btn_open = QtWidgets.QPushButton(mainWidget)
        self.btn_open.setGeometry(QtCore.QRect(110, 60, 141, 41))
        # 第一个按钮名字，和他的标题区分开来
        self.btn_open.setObjectName("btn_open")
        self.btn_img = QtWidgets.QPushButton(mainWidget)
        self.btn_img.setGeometry(QtCore.QRect(110, 120, 141, 41))
        # 第二个按钮名字
        self.btn_img.setObjectName("btn_img")

        self.retranslateUi(mainWidget)
        QtCore.QMetaObject.connectSlotsByName(mainWidget)

    def retranslateUi(self, mainWidget):
        _translate = QtCore.QCoreApplication.translate
        # 窗口标题
        mainWidget.setWindowTitle(_translate("mainWidget", "主窗体"))
        # 按钮标题
        self.btn_open.setText(_translate("mainWidget", "打开第二个widget"))
        self.btn_img.setText(_translate("mainWidget", "打开图片widget"))

class Main(QWidget, Ui_mainWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)


class Slave(QWidget, Ui_slaveWidget):
    def __init__(self):
        super(Slave, self).__init__()
        self.setupUi(self)

    def show_widget(self):
        # 展示当前widget
        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)

    w_main = Main()
    w_slave = Slave()

    w_main.show()
    # 打开其他窗口的方法,连接其它窗口的show函数
    w_main.btn_open.clicked.connect(w_slave.show_widget)

    sys.exit(app.exec_())