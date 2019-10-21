from PyQt5 import QtGui, QtWidgets
import sys
from Sudoku.modules.MainWindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon(r'Sudoku/images/svd.png'))
window = MainWindow()
window.show()
sys.exit(app.exec_())