from PyQt5 import QtCore, QtWidgets, QtPrintSupport

class PreviewDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('Preview')
        self.size(600, 400)
        vbox = QtWidgets.QVBoxLayout()
        hbox1 = QtWidgets.QHBoxLayout()
        btnZoomin = QtWidgets.QPushButton('+')
        btnZoomin.setFocusPolicy(QtCore.Qt.NoFocus)
        hbox1.addWidget(btnZoomin, alignment=QtCore.Qt.AlignLeft)
