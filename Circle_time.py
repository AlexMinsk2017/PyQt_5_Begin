from PyQt5 import QtWidgets
import sys, time

def on_clicked():
    time.sleep(10)

def new_on_clicked():
    button.setDisabled(True)
    for i in range(1, 21):
        QtWidgets.qApp.processEvents()
        time.sleep(1)
        print('step -', i)
    button.setDisabled(False)

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Run process')
button.resize(200, 50)
button.clicked.connect(new_on_clicked)
button.show()
sys.exit(app.exec_())