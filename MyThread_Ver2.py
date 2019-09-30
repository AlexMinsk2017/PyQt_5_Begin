from PyQt5 import QtWidgets, QtCore
import sys

class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False
        self.count = 0

    def run(self):
        self.running = True
        while self.running:
            self.count += 1
            self.mysignal.emit('count = %s' % self.count)
            self.sleep(1)

class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.label = QtWidgets.QLabel('Press key to run thread')
        self.btnStart = QtWidgets.QPushButton('Run thread')
        self.btnStop = QtWidgets.QPushButton('Stop thread')
        self.btnQuit = QtWidgets.QPushButton('&Close window')

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnStart)
        self.vbox.addWidget(self.btnStop)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)

        self.mythread = MyThread()

        self.btnStart.clicked.connect(self.on_start)
        self.btnStop.clicked.connect(self.on_stop)
        self.btnQuit.clicked.connect(QtWidgets.QApplication.exit)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def on_start(self):
        if not self.mythread.isRunning():
            self.mythread.start() #Запускаем поток

    def on_stop(self):
        self.mythread.running = False

    def on_change(self, s):
        self.label.setText(s)

    def closeEvent(self, event):
        self.hide()                     #Скрываем окно
        self.mythread.running = False   #Изменяем флаг
        self.mythread.wait(5000)        #Даем время
        event.accert()                  #Закрываем окно

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('Run and stop the threads')
    window.resize(400, 150)
    window.show()
    sys.exit(app.exec_())