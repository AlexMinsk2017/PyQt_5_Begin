from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('My first programm PyPt')
window.resize(400, 150)

label = QtWidgets.QLabel("<center> Hello, world!!!<center>")
btnQuit = QtWidgets.QPushButton("&Close")

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)

window.setLayout(vbox)

btnQuit.clicked.connect(app.quit)

#-------------------
window.show()
sys.exit(app.exec_())