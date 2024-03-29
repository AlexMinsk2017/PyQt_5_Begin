from PyQt5 import QtWidgets, QtCore, QtGui, QtPrintSupport
from Sudoku.modules.Widget import Widget
import re
from Sudoku.modules.previewdialog import PreviewDialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent, flags=QtCore.Qt.Window|QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle('Sudoku 2.0')
        self.setStyleSheet('QFrame QPushButton {font-size:10pt;font-family:Verdana;color:black;font-weight:bold;}'
                           'MyLabel {font-size:14pt;font-family:Verdana;border:1px solid #9AA6A7;}')
        self.settings = QtCore.QSettings('Hryb A.')
        self.printer = QtPrintSupport.QPrinter()

        self.sudoku = Widget()
        self.setCentralWidget(self.sudoku)

        menuBar = self.menuBar()
        toolBar = QtWidgets.QToolBar()

        myMenuFile = menuBar.addMenu('&File')
        action = myMenuFile.addAction(QtGui.QIcon(r'Sudoku/images/new.png'), '&New', self.sudoku.onClearAllCells,
                                      QtCore.Qt.CTRL + QtCore.Qt.Key_N)
        toolBar.addAction(action)
        action.setStatusTip('Create the new, empty game')

        action = myMenuFile.addAction(QtGui.QIcon(r'Sudoku/images/new.png'), '&Save game', self.onSave, QtCore.Qt.CTRL + QtCore.Qt.Key_S)
        toolBar.addAction(action)
        action.setStatusTip('Save game to file')
        action = myMenuFile.addAction(QtGui.QIcon(r'Sudoku/images/new.png'), '&Save game compact', self.onSaveMini)
        # toolBar.addAction(action)
        action.setStatusTip('Save game compact to file')

        myMenuFile.addSeparator()
        toolBar.addSeparator()

        action = myMenuFile.addAction('&Exit', QtWidgets.qApp.quit, QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        action.setStatusTip('Application shutdown')

        myMenuEdit = menuBar.addMenu('&Edit')
        #Copy/Paste
        action = myMenuEdit.addAction(QtGui.QIcon(r'images/copy.png'), "&Copy", self.onCopyData, QtCore.Qt.CTRL + QtCore.Qt.Key_C)
        toolBar.addAction(action)
        action.setStatusTip('Copy game to clipboard')
        action = myMenuEdit.addAction(QtGui.QIcon(r'images/copy.png'), "C&opy compact", self.onCopyDataMini)
        # toolBar.addAction(action)
        action.setStatusTip('Copy game compact')
        action = myMenuEdit.addAction(QtGui.QIcon(r'images/copy.png'), "Copy to &Excel", self.onCopyDataExcel)
        # toolBar.addAction(action)
        action.setStatusTip('Copy game to Excel')
        action = myMenuEdit.addAction(QtGui.QIcon(r'images/copy.png'), "Paste", self.onPasteData)
        # toolBar.addAction(action)
        action.setStatusTip('Paste game')
        action = myMenuEdit.addAction(QtGui.QIcon(r'images/copy.png'), "Paste from Excel", self.onPasteDataExcel)
        # toolBar.addAction(action)
        action.setStatusTip('Paste game from Excel')
        myMenuEdit.addSeparator()
        toolBar.addSeparator()
        ##################Print
        action = myMenuFile.addAction(QtGui.QIcon(r'images/copy.png'), 'Print...', self.onPrint, QtCore.Qt.CTRL + QtCore.Qt.Key_P)
        toolBar.addAction(action)
        action.setStatusTip('Print game')
        action = myMenuFile.addAction(QtGui.QIcon(r'images/copy.png'), 'Prievew...', self.onPreview)
        toolBar.addAction(action)
        action.setStatusTip('Prievew game')
        action = myMenuFile.addAction(QtGui.QIcon(r'images/copy.png'), 'Page setup...', self.onPageSetup)
        #toolBar.addAction(action)
        action.setStatusTip('Setup page')


        action = myMenuEdit.addAction('&Block', self.sudoku.onBlockCell, QtCore.Qt.Key_F2)
        action.setStatusTip('Blocked active cell')

        action = myMenuEdit.addAction(QtGui.QIcon(r'Sudoku/images/lock.png'), 'B&locked all', self.sudoku.onBlockCells,
                                      QtCore.Qt.Key_F3)
        toolBar.addAction(action)
        action.setStatusTip('Blocked all cells')

        action =myMenuEdit.addAction('&Unlock', self.sudoku.onClearBlockCell, QtCore.Qt.Key_F4)
        action.setStatusTip('Unlock active cell')

        action = myMenuEdit.addAction(QtGui.QIcon(r'Sudoku/images/unlock.png'), 'U&lock all',
                                      self.sudoku.onClearBlockCells, QtCore.Qt.Key_F5)
        toolBar.addAction(action)
        action.setStatusTip('Unlock all cells')

        myMenuAbout = menuBar.addMenu('&Help')
        action = myMenuAbout.addAction('About programme...', self.aboutInfo)
        action.setStatusTip('Get information about programme')
        action = myMenuAbout.addAction('About ...', QtWidgets.qApp.aboutQt)
        action.setStatusTip('To get information about Qt lib.')

        toolBar.setMovable(False)
        toolBar.setFloatable(False)
        self.addToolBar(toolBar)

        # statusBar = self.StatusBar()
        # statusBar.setSizeGribEnabled(False)
        # statusBar.showMessage('\"Sudoku\" greets you', 20000)
        # if self.settings.contains('X') and self.settings.contains('Y'):
        #     self.move(self.settings.value('X'), self.settings.value('Y'))

    def onPrint(self):
        pd = QtPrintSupport.QPrintDialog(self.printer, parent=self)
        pd.setOptions(QtPrintSupport.QAbstractPrintDialog.PrintToFile|QtPrintSupport.QAbstractPrintDialog.PrintSelection)
        if pd.exec() == QtWidgets.QDialog.Accepted:
            self.sudoku.print(self.printer)
    def onPreview(self):
        pd = PreviewDialog(self)
        pd.exec()
    def onPageSetup(self):
        pd = QtPrintSupport.QPageSetupDialog(self.printer, parent=self)
        pd.exec()

    def onOpenFile(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', QtCore.QDir.homePath(), 'Sudoku (*.svd)')[0]
        if fileName:
            data = ''
            try:
                with open(fileName, newline='') as f:
                    data = f.read()
            except:
                QtWidgets.QMessageBox.information(self, 'Sudoku', 'Don\'t open file')
                return
            if len(data) > 2:
                data = data[:-1]
            if len(data) == 81 or len(data) == 162:
                r = re.compile(r'[^0-9]')
                if not r.match(data):
                    self.sudoku.setDataAllCells(data)
                    return
            self.dataErrorMsg()
    def onSave(self):
        self.saveSVDFile(self.sudoku.getDataAllCells())
    def onSaveMini(self):
        self.saveSVDFile(self.sudoku.getDataAllCellsMini())
    def saveSVDFile(self, data):
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Select file', QtCore.QDir.homePath(), 'Sudoku (*.svd)')[0]
        if fileName:
            try:
                with open(fileName, mode='w', newline='') as f:
                    f.write(data)
                self.statusBar().showMessage('File saved')
            except:
                QtWidgets.QMessageBox.information(self, 'Sudoku', '')

    def onCopyData(self):
        QtWidgets.QApplication.clipboard().setText(self.sudoku.getDataAllCells())
    def onCopyDataMini(self):
        QtWidgets.QApplication.clipboard().setText(self.sudoku.getDataAllCellsMini())
    def onCopyDataExcel(self):
        QtWidgets.QApplication.clipboard().setText(self.sudoku.getDataAllCellsExcel())
    def onPasteData(self):
        data = QtWidgets.QApplication.clipboard().text()
        if data:
            if len(data) == 81 or len(data) == 162:
                r = re.compile(r'[^0-9]')
                if not r.match(data):
                    self.sudoku.setDataAllCells(data)
                    return
        self.dataErrorMsg()
    def onPasteDataExcel(self):
        data = QtWidgets.QApplication.clipboard().text()
        if data:
            data = data.replace('\r', '')
            r = re.compile(r'([0-9]?[\t\n]){81}')
            if r.match(data):
                result = []
                if data[-1] == '\n':
                    data = data[:-1]
                dl = data.split('\n')
                for sl in dl:
                    dli = data.split('\t')
                    for sli in dli:
                        if len(sli) == '0':
                            result.append('00')
                        else:
                            result.append('0' + sli[0])
                data = ''.join(result)
                self.sudoku.setDataAllCells(data)
                return
        self.dataErrorMsg()

    def dataErrorMsg(self):
        QtWidgets.QMessageBox.information(self, 'Sudoku', 'Unreadble data file format')

    def closeEvent(self, evt):
        g = self.geometry()
        self.settings.setValue('X', g.left())
        self.settings.setValue('Y', g.top())

    def aboutInfo(self):
        QtWidgets.QMessageBox.about(self, 'About programm', '<center> \"Sudoku\" v2.0<br><br>'
                                    'Programm for viewing and editing sudoku <br><br>'
                                    '(c) Hryb 2019')