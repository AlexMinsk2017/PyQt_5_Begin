from PyQt5 import QtWidgets, QtCore
import MainWindow
import sys

class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self.myWidget = MainWindow.MyWindow()
        self.myWidget.vbox.setContentsMargins(0, 0, 0, 0)
        self.button = QtWidgets.QPushButton('&Change text')

        mainBox = QtWidgets.QVBoxLayout()
        mainBox.addWidget(self.myWidget)
        mainBox.addWidget(self.button)
        self.setLayout(mainBox)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.myWidget.label.setText('New text')
        self.button.setDisabled(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle('Преимущество ООП')
    window.resize(450, 150)
    window.show()
    sys.exit(app.exec_())