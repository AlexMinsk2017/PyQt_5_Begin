from PyQt5 import QtWidgets, QtCore
import sys

class MyWindow(QtWidgets.QWidget):

    mysignal = QtCore.pyqtSignal(int, int)

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle('Generate signal from programm')
        self.resize(450, 100)

        self.button1 = QtWidgets.QPushButton('Press me')
        self.button2 = QtWidgets.QPushButton('Button 2')
        self.btnQuit = QtWidgets.QPushButton('&Close')

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.button1)
        self.vbox.addWidget(self.button2)
        self.vbox.addWidget(self.btnQuit)

        self.setLayout(self.vbox)

        self.button1.clicked.connect(lambda : self.on_clicked_button1(10))
        self.button2.clicked.connect(self.on_clicked_button2)
        self.mysignal.connect(self.on_mysignal)
        self.btnQuit.clicked.connect(QtWidgets.QApplication.exit)

    def on_clicked_button1(self, x = 0):
        print('Pressed button 1')
        print('x = ', x)
        self.button2.clicked[bool].emit(False)
        self.mysignal.emit(10, 20)

    def on_clicked_button2(self):
        print('Pressed button 2')

    def on_mysignal(self, x, y):
        print('worked user\'s signal "mysignal()"')
        print('x= ', x, ' y= ', y)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())