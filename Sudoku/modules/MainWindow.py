from PyQt5 import QtWidgets, QtCore, QtGui, QtPrintSupport
from Sudoku.modules.Widget import Widget

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

        myMenuFile.addSeparator()
        toolBar.addSeparator()

        action = myMenuFile.addAction('&Exit', QtWidgets.qApp.quit, QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        action.setStatusTip('Application shutdown')

        myMenuEdit = menuBar.addMenu('&Edit')
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

    def closeEvent(self, evt):
        g = self.geometry()
        self.settings.setValue('X', g.left())
        self.settings.setValue('Y', g.top())

    def aboutInfo(self):
        QtWidgets.QMessageBox.about(self, 'About programm', '<center> \"Sudoku\" v2.0<br><br>'
                                    'Programm for viewing and editing sudoku <br><br>'
                                    '(c) Hryb 2019')