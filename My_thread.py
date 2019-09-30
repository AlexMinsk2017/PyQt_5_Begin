from PyQt5 import QtWidgets, QtCore
import sys, time

class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        for i in range(1,10):
            self.sleep(1)
            self.mysignal.emit('i = %s' % i)

class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.label = QtWidgets.QLabel('Press button for run thread')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button = QtWidgets.QPushButton('Run process')
        self.btnQuit = QtWidgets.QPushButton('&Close window')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)

        self.mythread = MyThread()

        self.button.clicked.connect(self.on_clicked)
        self.btnQuit.clicked.connect(QtWidgets.QApplication.exit)
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def on_clicked(self):
        self.button.setDisabled(True)
        self.btnQuit.setDisabled(True)
        self.mythread.start()

    def on_started(self):
        self.label.setText('Run method "on_started()"')

    def on_finished(self):
        self.label.setText('Run method "on_finished()"')
        self.button.setDisabled(False)
        self.btnQuit.setDisabled(False)

    def on_change(self, s):
        self.label.setText(s)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('Using QThread class')
    window.resize(350, 100)
    window.show()
    sys.exit(app.exec_())