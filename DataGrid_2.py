from PyQt5 import QtWidgets, QtCore, QtSql
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QTableView()
window.setWindowTitle('Table')

con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()

sqm = QtSql.QSqlQueryModel(parent=window)
sqm.setQuery('select * from good by goodname')
sqm.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
sqm.setHeaderData(2, QtCore.Qt.Horizontal, 'Quantity')

window.setModel(sqm)

# window.hideColumn(0)
window.setColumnWidth(1, 150)
window.setColumnWidth(2, 60)

window.resize(260, 160)

window.show()
sys.exit(app.exec_())