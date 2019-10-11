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
        self.sldPosition.valueChanged.connect(self.mplPlayer.setPosition)
        self.mplPlayer.positionChanged.connect(self.sldPosition.setValue)
        self.mplPlayer.mediaStatusChanged.connect(self.showMetadata)
        self.sldPosition.setEnabled(False)
        vbox.addWidget(self.sldPosition)

        hbox = QtWidgets.QHBoxLayout()

        self.btnPlay = QtWidgets.QPushButton('&Play')
        self.btnPlay.clicked.connect(self.mplPlayer.play)
        self.btnPlay.setEnabled(False)
        hbox.addWidget(self.btnPlay)
        self.btnPause = QtWidgets.QPushButton('P&ause')
        self.btnPause.clicked.connect(self.mplPlayer.pause)
        self.btnPause.setEnabled(False)
        hbox.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton('&Stop')
        self.btnStop.clicked.connect(self.mplPlayer.stop)
        self.btnStop.setEnabled(False)
        hbox.addWidget(self.btnStop)
        vbox.addLayout(hbox)
        # volume control
        hbox = QtWidgets.QHBoxLayout()
        lblVolume = QtWidgets.QLabel('&Volume')
        hbox.addWidget(lblVolume)
        sldVolume = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        sldVolume.setRange(0, 100)
        sldVolume.setTickPosition(QtWidgets.QSlider.TicksAbove)
        sldVolume.setTickInterval(10)
        lblVolume.setBuddy(sldVolume)
        sldVolume.valueChanged.connect(self.mplPlayer.setVolume)
        hbox.addWidget(sldVolume)
        btnMute = QtWidgets.QPushButton('&Mute')
        btnMute.setCheckable(True)
        btnMute.toggled.connect(self.mplPlayer.setMuted)
        hbox.addWidget(btnMute)
        vbox.addLayout(hbox)

        self.txtOutput = QtWidgets.QTextEdit()
        self.txtOutput.setReadOnly(True)
        vbox.addWidget(self.txtOutput)

        #main vbox
        self.setLayout(vbox)
        self.resize(800, 300)

    def showMetadata(self, state):
        self.txtOutput.clear()

    def openFile(self):
        file = QtWidgets.QFileDialog.getOpenFileUrl(parent=self, caption='Select audio file', filter='Audio files (*.mp3 *.ac3)')
        self.mplPlayer.setMedia(QtMultimedia.QMediaContent(file[0]))

    def initPlayer(self, state):
        if state == QtMultimedia.QMediaPlayer.LoadedMedia:

            self.mplPlayer.stop()
            self.btnPlay.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.sldPosition.setEnabled(True)
            self.sldPosition.setMaximum(self.mplPlayer.duration())
        elif state == QtMultimedia.QMediaPlayer.EndOfMedia:

            self.mplPlayer.stop()
            self.sldPosition.setValue(0)
            self.sldPosition.setEnabled(False)
            self.btnPlay.setEnabled(False)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)
        elif state == QtMultimedia.QMediaPlayer.NoMedia or state == QtMultimedia.QMediaPlayer.InvalidMedia:

            self.sldPosition.setValue(0)
            self.sldPosition.setEnabled(False)
            self.btnPlay.setEnabled(False)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)

    def setPlayerState(self, state):
        if state == QtMultimedia.QMediaPlayer.StoppedState:

            self.sldPosition.setValue(0)
            self.btnPlay.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)
        elif state == QtMultimedia.QMediaPlayer.PlayingState:

            self.btnPlay.setEnabled(False)
            self.btnPause.setEnabled(True)
            self.btnStop.setEnabled(True)
        elif state == QtMultimedia.QMediaPlayer.PausedState:

            self.btnPlay.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())