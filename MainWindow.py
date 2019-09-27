from PyQt5 import QtCore, QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.label = QtWidgets.QLabel('Hello world')
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.btQuit = QtWidgets.QPushButton('&Close window')

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btQuit)

        self.setLayout(self.vbox)

        self.btQuit.clicked.connect(QtWidgets.qApp.quit)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('ООП стиль')
    window.resize(450, 150)

    window.show()
    sys.exit(app.exec_())