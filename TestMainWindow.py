from PyQt5 import QtWidgets, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Test window')
window.resize(500, 250)
# window.setWindowFlags(QtCore.Qt.Tool)
desktop = QtWidgets.QApplication.desktop()
x = (desktop.width() - window.width())//4
y = (desktop.height() - window.height())//4
window.move(x, y)
window.show()
sys.exit(app.exec_())