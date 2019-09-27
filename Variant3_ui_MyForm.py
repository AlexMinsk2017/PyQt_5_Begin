from PyQt5 import QtWidgets
import sys, ui_MyForm

class MyWindow(QtWidgets.QMainWindow, ui_MyForm.Ui_NewForm):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())