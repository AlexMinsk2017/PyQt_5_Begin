from PyQt5 import QtWidgets
import sys

class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, id, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.id = id
    def focusInEvent(self, ev):
        print('Set focus on field: ', self.id)
        QtWidgets.QLineEdit.focusInEvent(self, ev)
    def focusOutEvent(self, ev):
        print('Lost focus field: ', self.id)
        QtWidgets.QLineEdit.focusOutEvent(self, ev)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(350, 100)
        self.setWindowTitle('Change focus')

        self.button = QtWidgets.QPushButton('Set focus on field 2')
        self.btnQuit = QtWidgets.QPushButton('&Close')
        self.line1 = MyLineEdit(1)
        self.line2 = MyLineEdit(2)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.line2)
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.btnQuit)

        self.setLayout(self.vbox)

        self.btnQuit.clicked.connect(QtWidgets.QApplication.exit)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.line2.setFocus()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
