from PyQt5 import QtWidgets

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
