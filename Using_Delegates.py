from PyQt5 import QtWidgets, QtCore, QtGui
import sys

#Create Delegate
class SpinBoxDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, options, index):
        editor = QtWidgets.QSpinBox(parent)
        editor.setFrame(False)
        editor.setMinimum(0)
        editor.setSingleStep(1)
        return editor
    def setEditorData(self, editor, index):
        value = int(index.model().data(index, QtCore.Qt.EditRole))
        editor.setValue(value)
    def updateEditorGeometry(self, editor, options, index):
        editor.setGeometry(options.rect)
    def setModelData(self, editor, model, index):
        value = str(editor.value())
        model.setData(index, value, QtCore.Qt.EditRole)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QTableView()
window.setWindowTitle('Use delegate')
sti = QtGui.QStandardItemModel(parent=window)
lst1 = ['Diskette', 'Paper for printer', 'printer drum']
lst2 = ['10', '5', '8']
for row in range(0,3):
    item1 = QtGui.QStandardItem(lst1[row])
    item2 = QtGui.QStandardItem(lst2[row])
    sti.appendRow([item1, item2])
sti.setHorizontalHeaderLabels(['Goods', 'Quantity'])
window.setModel(sti)
#append Delegate
window.setItemDelegateForColumn(1, SpinBoxDelegate())
window.setColumnWidth(0, 250)
window.resize(450, 250)
window.show()
sys.exit(app.exec_())