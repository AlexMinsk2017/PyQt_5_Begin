from PyQt5 import QtWidgets, QtCore
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(350, 100)
    def event(self, ev):
        if ev.type() == QtCore.QEvent.KeyPress:
            print('Pressed key on keyboard: ', ev.key(), ', text: ', ev.text())
        # elif ev.type() == QtCore.QEvent.Close:
        #     print('Window closed')
        elif ev.type() == QtCore.QEvent.MouseButtonPress:
            print('Click mouse. Coordinate: ', ev.x(), ev.y())
        elif ev.type() == QtCore.QEvent.MouseButtonDblClick:
            print('Double click mouse. Coordinate: ', ev.x(), ev.y())
        return QtWidgets.QWidget.event(self, ev)
    def closeEvent(self, ev):
        result == QtWidgets.QMessageBox.question(self,
                                                 'Confirmation of closing the window',
                                                 'Do you really close the window?',
                                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                 QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            ev.accert()
            QtWidgets.QWidget.closeEvent(self, ev)
        else:
            ev.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
