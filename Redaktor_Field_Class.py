from PyQt5 import QtWidgets, QtCore, QtSql
import sys

class conDatabase():

    def __init__(self):
        self.con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.con.setDatabaseName('data.sqlite')

    def stmCreate(self, window):
        stm = QtSql.QSqlTableModel(parent=window)
        stm.setTable('good')
        stm.setSort(1, QtCore.Qt.AscendingOrder)
        stm.select()
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Quantity')
        return stm

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        QtWidgets.QWidget()
        self.setWindowTitle('table grid 2')

        conDt = conDatabase()
        self.con = conDt.con
        self.con.open()
        self.stm = conDt.stmCreate(self)
        # self.conDt.stmCreate(self)
        # self.stm = self.conDt.stm

        self.vbox = QtWidgets.QVBoxLayout()
        self.tv = QtWidgets.QTableView()
        self.tv.setModel(self.stm)
        self.tv.setItemDelegate(QtSql.QSqlRelationalDelegate(self.tv))
        self.tv.hideColumn(0)
        self.tv.setColumnWidth(1, 350)
        self.tv.setColumnWidth(2, 100)
        self.vbox.addWidget(self.tv)

        self.btnAdd = QtWidgets.QPushButton('&Add record')
        self.btnAdd.clicked.connect(self.addRecord)
        self.vbox.addWidget(self.btnAdd)

        self.btnDel = QtWidgets.QPushButton('&Delete record')
        # self.btnDel.clicked.connect(lambda: self.delRecord(stm, self.tv))
        self.btnDel.clicked.connect(self.delRecord)
        self.vbox.addWidget(self.btnDel)

        self.setLayout(self.vbox)

    def addRecord(self):
        self.stm.insertRow(self.stm.rowCount())

    def delRecord(self):
        self.stm.removeRow(self.tv.currentIndex().row())
        self.stm.select()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())