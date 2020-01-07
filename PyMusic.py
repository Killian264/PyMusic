from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import shutil
configLoc = "./config.json"
from ConfigFunctions import *
import MusicClass
from os.path import isfile, join
from os import *
import sys
from PyQt5.QtGui import QColor, QBrush

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # gets user settings
        self.getSettings()

        # setup play state
        self.isPlaying = False # 0 is paused 1 is playing
        # gets the playlist of songs from folder see func
        self.getPlaylist()
        # player stuff
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.setVolume(self.volume)

        # setupUi is all stuff made in QtDesigner
        self.setupUi()
        # connects basically setting functions to event handlers
        self.connects()
        # very important
        self.changeSpeakerImg()

        self.model = QtGui.QStandardItemModel()
        self.songView.setModel(self.model)


        self.getMusicList()
        # thingies
        # songView
        # previous button
        # play button
        # next button
        # progress bar // song progress bar
        # speaker Image
        # Audio Slider
        # Menubar

    # gets settings and change object state this will probably be chagned later so its a function
    def getSettings(self):
        # configLoc does not need to be passed
        self.volume, self.musicLoc = getSettings(configLoc)

    # this will be changed out later for a more robust loader of multiple songs
    def getPlaylist(self):
        self.playlist = QMediaPlaylist()

    def addSongToView(self, songName):
        songStandardItem = QtGui.QStandardItem(songName.split('.')[0])
        songStandardItem.setEditable(False)
        color = QColor(20, 20, 20, 130)
        #color = QColor(100, 100, 100, 130)
        brush = QBrush()
        brush.setColor(color)
        brush.setStyle(1)
        songStandardItem.setBackground(brush)
        #color = QColor("white")
        #brush = QBrush()
        #brush.setColor(color)
        #brush.setStyle(1)
        #songStandardItem.setForeground(brush)
        self.model.appendRow(songStandardItem)

    # build out and allow for dirs I could use recursion to make this possible
    def getMusicList(self):
        # this makes a list, gets all files in directory, then makes class with item and adds to list and to fileview
        self.musicList = []
        onlyfiles = [f for f in listdir(self.musicLoc) if isfile(join(self.musicLoc, f))]
        for music in onlyfiles:
            musicClass = MusicClass.Song(self.musicLoc, music)
            self.musicList.append(musicClass)
            self.addSongToView(music)


    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(913, 642)

        # size policy
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet("background-color: rgb(36,36,36);\n""color: white;")
        self.setDocumentMode(True)

        # some layouts
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        # song view
        self.songView = QtWidgets.QListView(self.centralwidget)
        self.songView.setObjectName("songView")
        self.songView.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.songView)

        # previous button
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previous.sizePolicy().hasHeightForWidth())
        self.previous.setSizePolicy(sizePolicy)
        self.previous.setStyleSheet("background-color: rgb(36,36,36);\n""border: none;")
        self.previous.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous.setIcon(icon)
        self.previous.setObjectName("previous")
        self.horizontalLayout.addWidget(self.previous)

        # play button
        self.play = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play.sizePolicy().hasHeightForWidth())
        self.play.setSizePolicy(sizePolicy)
        self.play.setStyleSheet("border: none;")
        self.play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon1)
        self.play.setObjectName("play")
        self.horizontalLayout.addWidget(self.play)

        # forward button
        self.forward = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forward.sizePolicy().hasHeightForWidth())
        self.forward.setSizePolicy(sizePolicy)
        self.forward.setStyleSheet("border: none;")
        self.forward.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward.setIcon(icon2)
        self.forward.setObjectName("forward")
        self.horizontalLayout.addWidget(self.forward)

        # song progress slider
        self.songSlider = QtWidgets.QSlider(self.centralwidget)
        self.songSlider.setStyleSheet(".QSlider {\n"
                                            "    min-height: 20px;\n"
                                            "    max-height: 20px;\n"
                                            "}\n"
                                            "\n"
                                            ".QSlider::groove:horizontal {\n"
                                            "    height: 2px;\n"
                                            "    background: #d1d1cf;\n"
                                            "}\n"
                                            "\n"
                                            ".QSlider::handle:horizontal {\n"
                                            "    background: white;\n"
                                            "    width: 10px;\n"
                                            "    height: 10px;\n"
                                            "    margin: -1px 0px;\n"
                                            "}")
        self.songSlider.setOrientation(QtCore.Qt.Horizontal)
        self.songSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.songSlider)


        # speaker image label
        self.speakerImage = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speakerImage.sizePolicy().hasHeightForWidth())
        self.speakerImage.setSizePolicy(sizePolicy)
        self.speakerImage.setMaximumSize(QtCore.QSize(20, 20))
        self.speakerImage.setText("")
        self.speakerImage.setPixmap(QtGui.QPixmap(":/icons/speaker-max.png"))
        self.speakerImage.setScaledContents(True)
        self.speakerImage.setObjectName("speakerImage")
        self.horizontalLayout.addWidget(self.speakerImage)
        self.audioSlider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioSlider.sizePolicy().hasHeightForWidth())

        # Audio Slider
        self.audioSlider.setSizePolicy(sizePolicy)
        self.audioSlider.setStyleSheet(".QSlider {\n"
        "    min-height: 20px;\n"
        "    max-height: 20px;\n"
        "}\n"
        "\n"
        ".QSlider::groove:horizontal {\n"
        "    height: 5px;\n"
        "    background: #393939;\n"
        "}\n"
        "\n"
        ".QSlider::handle:horizontal {\n"
        "    background: white;\n"
        "    width: 5px;\n"
        "    height: 100px;\n"
        "    margin: -24px 0px;\n"
        "}")
        self.audioSlider.setOrientation(QtCore.Qt.Horizontal)
        self.audioSlider.setObjectName("audioSlider")
        self.horizontalLayout.addWidget(self.audioSlider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)

        # menubar
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 913, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.fileMenuOpen = QtWidgets.QAction(self)
        self.fileMenuOpen.setObjectName("fileMenuOpen")
        self.changeDefaultFolder = QtWidgets.QAction(self)
        self.changeDefaultFolder.setObjectName("changeDefaultFolder")
        self.menuFile.addAction(self.fileMenuOpen)
        self.menuFile.addAction(self.changeDefaultFolder)
        self.menubar.addAction(self.menuFile.menuAction())

        # not sure why retranslateUi is split up
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    # naming things? this was made by the QtDesigner
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "PyMusic"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.fileMenuOpen.setText(_translate("MainWindow", "Open Music File"))
        self.changeDefaultFolder.setText(_translate("MainWindow", "Change Music Folder"))

    # basically event listeners for changes
    def connects(self):
        self.previous.clicked.connect(self.prevSong)
        self.play.clicked.connect(self.changeSongState)
        self.forward.clicked.connect(self.nextSong)
        self.audioSlider.valueChanged.connect(self.changeAudioVolume)
        self.songSlider.sliderMoved.connect(self.changeSongPosition)
        #self.songSlider.valueChanged.connect(self.changeSongPosition)
        #self.player.positionChanged.connect(self.changeSliderPosition)

        self.fileMenuOpen.triggered.connect(self.getFile)
        self.changeDefaultFolder.triggered.connect(self.getDirectory)
        self.songView.doubleClicked.connect(self.playSongAtIndex)


    # File Thingies
    def getFile(self):
        # open dialog, check if user has file, move file to music Folder
        fileInfo = QFileDialog.getOpenFileName(self, 'Open File')
        currentLoc, typeOrSomething = fileInfo
        if not currentLoc == '':
            shutil.move(currentLoc, self.musicLoc)

        fileName = currentLoc.split('/')[-1]
        musicClass = MusicClass.Song(self.musicLoc, fileName)
        self.musicList.append(musicClass)
        self.addSongToView(fileName)

    def getDirectory(self):
        # open dialog, check if user has file, move file to music Folder
        dir = QFileDialog.getExistingDirectory(self, "Select Directory")
        if not dir == '':
            self.musicLoc = dir
            updateConfig(self.volume, dir, configLoc)

    # song slider change connects
    # these don't work properly fix later
    def changeSongPosition(self, position):
        self.player.setPosition(position * (self.player.duration() / 100))

    def changeSliderPosition(self, position):
        self.songSlider.setSliderPosition(position / (self.player.duration() / 100))

    # audio slider change connect
    def changeAudioVolume(self):
        self.volume = self.audioSlider.value()
        self.player.setVolume(self.volume)
        self.changeSpeakerImg()
        updateConfig(self.volume, self.musicLoc, configLoc)

    # changes speaker image based on volume
    def changeSpeakerImg(self):
        img = QtGui.QPixmap(":/icons/speaker-none.png")
        if self.volume > 70:
            img = QtGui.QPixmap(":/icons/speaker-max.png")
        elif self.volume < 70 and self.volume > 30:
            img = QtGui.QPixmap(":/icons/speaker-med.png")
        elif self.volume < 30 and self.volume > 0:
            img = QtGui.QPixmap(":/icons/speaker-low.png")
        self.speakerImage.setText("")
        self.speakerImage.setPixmap(img)

    # Prev song // plan is to either load songs into array of file locations
    def prevSong(self):
        print("play prev")

    def nextSong(self):
        print("play next")

    def playSongAtIndex(self, index):
        # get music list, get MusicClass at row clicked, return MediaContentClass of that index
        song = self.musicList[index.row()].returnMediaContent()
        # remove song and add new song then play
        pos = self.playlist.currentIndex()
        self.playlist.removeMedia(pos)
        self.playlist.insertMedia(pos, song)
        self.playSong()


    # checks song state and changes it
    def changeSongState(self):
        # stop may be added later
        if not self.isPlaying:
            self.playSong()
        elif self.isPlaying:
            self.pauseSong()

    def playSong(self):
        self.player.play()
        self.isPlaying = True
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon)

    def pauseSong(self):
        self.player.pause()
        self.isPlaying = False
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon)

# does stuff
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        win = MainWindow()
        win.show()
        sys.exit(app.exec_())


