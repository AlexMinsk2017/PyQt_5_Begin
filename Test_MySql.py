from PyQt5 import QtWidgets, QtSql
import sys

app = QtWidgets.QApplication(sys.argv)

conl = QtSql.QSqlDatabase.addDatabase('QSQLITE')
conl.setDatabaseName('data.sqlite')
conl.open()
if 'good' not in conl.tables():
    query = QtSql.QSqlQuery()
    query.exec('create table good(id integer primary key autoincrement, goodname text, goodcount integer )')

query = QtSql.QSqlQuery()
query.prepare('insert into good values(null, ?, ?)')
query.addBindValue('Diskette')
query.addBindValue(10)
query.exec_()

query = QtSql.QSqlQuery()
query.prepare('insert into good values(null, :name, :count)')
query.bindValue(':name', 'Flash disk')
query.bindValue(':count', 15)
query.exec_()

query = QtSql.QSqlQuery()
query.prepare('insert into good values(null, :name, :count)')
lst1 = ['Paper', 'Photopaper', 'Cartridge']
lst2 = [10, 5, 3]
query.bindValue(':name', lst1)
query.bindValue(':count', lst2)
query.execBatch()

conl.close()
