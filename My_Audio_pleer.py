from PyQt5 import QtWidgets, QtCore, QtMultimedia
import sys

class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window|QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle('Mediaplayer')
        #class mediaplayer
        self.mplPlayer = QtMultimedia.QMediaPlayer()
        self.mplPlayer.setVolume(50)
        self.mplPlayer.mediaStatusChanged.connect(self.initPlayer)
        vbox = QtWidgets.QVBoxLayout()

        btnOpen = QtWidgets.QPushButton('&Open file...')
        btnOpen.clicked.connect(self.openFile)
        vbox.addWidget(btnOpen)

        #Комопоненты управления медиа
        self.sldPosition = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sldPosition.setMinimum(0)
        self.sldPosition.valueChanged.connect.(self.mplPlayer.setPosition)
        self.mplPlayer.positionChanged.connect.(self.sldPosition.setValue)

        #main vbox
        self.setLayout(vbox)
        self.resize(400, 150)

    def openFile(self):
        return

    def initPlayer(self, state):
        return

    def setPlayerState(self, state):
        return

if __name__ == '__main__'
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())