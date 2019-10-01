from PyQt5 import QtWidgets, QtCore
import sys

class Thread1(QtCore.QThread):
    s1 = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.count = 0

    def run(self) :
        self.exec_()

    def on_start(self):
        self.count += 1
        self.s1.emit(self.count)

class Thread2(QtCore.QThread):
    s2 = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        self.exec_()

    def on_change(self, i):
        i += 10
        self.s2.emit('%d' % i)

class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel('Press key')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button = QtWidgets.QPushButton('Generate signal')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)

        self.thread1 = Thread1()
        self.thread2 = Thread2()

        self.thread1.start()
        self.thread2.start()

        self.button.clicked.connect(self.thread1.on_start)
        self.thread1.s1.connect(self.thread2.on_change)
        self.thread2.s2.connect(self.on_thread2_s2)

    def on_thread2_s2(self, s):
        self.label.setText(s)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('Change signal')
    window.resize(400, 150)
    window.show()
    sys.exit(app.exec_())

