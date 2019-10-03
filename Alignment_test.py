from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('QFormLayout')
window.resize(400, 150)

lineEdit = QtWidgets.QLineEdit()
textEdit = QtWidgets.QTextEdit()
button1 = QtWidgets.QPushButton("&Send")
button2 = QtWidgets.QPushButton('&Clear')

radio1 = QtWidgets.QRadioButton('&Yes')
radio2 = QtWidgets.QRadioButton('&No')
box = QtWidgets.QGroupBox('Do you know Python language?')
box.setCheckable(True)
box.setChecked(True)
hbox_rb = QtWidgets.QHBoxLayout()
hbox_rb.addWidget(radio1)
hbox_rb.addWidget(radio2)
box.setLayout(hbox_rb)

hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)

tab = QtWidgets.QTabWidget()
tab.addTab(hbox, 'Sheet 1')
tab.addTab(QtWidgets.QLabel('Content of sheet 2'), 'Sheet 2')

form = QtWidgets.QFormLayout()
form.addRow(tab)
form.addRow('&Name: ', lineEdit)
form.addRow('&Description: ', textEdit)
form.addRow(box)
# form.addRow(hbox)

window.setLayout(form)

window.show()
sys.exit(app.exec_())
