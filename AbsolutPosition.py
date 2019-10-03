from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Absolut position')
window.resize(300, 120)
label = QtWidgets.QLabel('Text legent', window)
button = QtWidgets.QPushButton('Text on button', window)
label.setGeometry(10, 10, 280, 60)
button.resize(150,30)
button.move(10, 80)
window.show()
sys.exit(app.exec_())