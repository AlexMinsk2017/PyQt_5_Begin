from PyQt5 import QtWidgets, QtCore, QtSql
import sys

class MyWindow(QtWidgets.QTableView):
    def __init__(self, parent=None):
        QtWidgets.QTableView.__init__(self, parent)
        self.setWindowTitle('Table')

        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName('data.sqlite')
        con.open()

        sqm = QtSql.QSqlQueryModel(parent=self)
        sqm.setQuery('select * from good by goodname')
        sqm.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
        sqm.setHeaderData(2, QtCore.Qt.Horizontal, 'Quantity')

        self.setModel(sqm)

        self.hideColumn(0)
        self.setColumnWidth(1, 150)
        self.setColumnWidth(2, 60)

        self.resize(260, 160)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
