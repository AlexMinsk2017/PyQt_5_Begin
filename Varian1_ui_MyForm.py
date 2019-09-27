from PyQt5 import QtWidgets
import sys, ui_MyForm

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = ui_MyForm.Ui_NewForm()
ui.setupUi(window)
ui.btnQuit.clicked.connect(QtWidgets.qApp.quit)

window.show()
sys.exit(app.exec_())