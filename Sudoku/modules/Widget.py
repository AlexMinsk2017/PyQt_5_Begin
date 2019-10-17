from PyQt5 import QtWidgets, QtCore, QtGui
from Sudoku.modules.MyLabel import MyLabel
import sys

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        vBoxMain = QtWidgets.QVBoxLayout()
        frame1 = QtWidgets.QFrame()
        frame1.setStyleSheet('background-color:#9AA6A7;border:1px solid #9AA6A7;')
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(0)
        idColor = (3, 4, 5, 12, 13, 14, 21, 22, 23,
                   27, 28, 29, 36, 37, 38, 45, 46, 47,
                   33, 34, 35, 42, 43, 44, 51, 52, 53,
                   57, 58, 59, 66, 67, 68, 75, 76, 77)
        self.cells = [MyLabel(i, MyLabel.colorGrey if i in idColor else MyLabel.colorOrange) for i in range(0, 81)]
        self.cells[0].setCellFocus()
        self.idCellInFocus = 0
        i = 0
        for j in range(0, 9):
            for k in range(0, 9):
                grid.addWidget(self.cells[i], j, k)
                i += 1
        for cell in self.cells:
            cell.changeCellFocus.connect(self.onChangeCellFocus)
        frame1.setLayout(grid)
        vBoxMain.addWidget(frame1, alignment=QtCore.Qt.AlignHCenter)

        frame2 = QtWidgets.QFrame()
        frame2.setFixedSize(272, 45)
        hbox = QtWidgets.QHBoxLayout()
        hbox.setSpacing(1)
        btns = []
        for i in range(1, 10):
            btn = QtWidgets.QPushButton(str(i))
            btn.setFixedSize(27, 27)
            btn.setFocusPolicy(QtCore.Qt.NoFocus)
            btns.append(btn)
        btn = QtWidgets.QPushButton('X')
        btn.setFixedSize(27, 27)
        btns.append(btn)
        for btn in btns:
            hbox.addWidget(btn)

        #-------------------
        frame2.setLayout(hbox)
        vBoxMain.addWidget(frame2, alignment=QtCore.Qt.AlignHCenter)
        self.setLayout(vBoxMain)

    def onChangeCellFocus(self):
        return

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = Widget()
    windows.show()
    sys.exit(app.exec_())
