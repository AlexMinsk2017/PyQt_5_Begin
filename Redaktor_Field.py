from PyQt5 import QtCore, QtWidgets, QtSql
import sys

def addRecord():
    stm.insertRow(stm.rowCount())
def delRecord():
    stm.removeRow(tv.currentIndex().row())
    stm.select()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('record table')

con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()

stm = QtSql.QSqlTableModel(parent=window)
stm.setTable('good')
stm.setSort(1, QtCore.Qt.AscendingOrder)
stm.select()

stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Quantity')

vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)
tv.hideColumn(0)
tv.setColumnWidth(1, 350)
tv.setColumnWidth(2, 100)
vbox.addWidget(tv)

btnAdd = QtWidgets.QPushButton('&Add record')
btnAdd.clicked.connect(addRecord)
vbox.addWidget(btnAdd)

btnDel = QtWidgets.QPushButton('&Delete record')
btnDel.clicked.connect(delRecord)
vbox.addWidget(btnDel)

window.setLayout(vbox)
window.resize(450, 350)
window.show()
sys.exit(app.exec_())