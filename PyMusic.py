from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import icons_rc
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import shutil
configLoc = "./config.json"
import ConfigFunctions
import MusicClass
from os.path import isfile, join
from os import *
import sys
import UI
import CustomSlider

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # gets user settings
        self.getSettings()

        # setup play state
        self.isPlaying = False # 0 is paused 1 is playing
        # index of currently playing song -- used for
        self.currentSong = 0
        # gets the playlist of songs from folder see func
        self.getPlaylist()
        # player stuff
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.setVolume(self.volume)

        # setupUi is all stuff made in QtDesigner
        UI.setupUi(self)
        # connects basically setting functions to event handlers
        self.connects()
        # very important
        self.changeSpeakerImg()

        self.getMusicList()

# MORE INIT STUFF
    # gets settings and change object state this will probably be chagned later so its a function
    def getSettings(self):
        # configLoc does not need to be passed
        self.volume, self.musicLoc = ConfigFunctions.getSettings(configLoc)

    # this will be changed out later for a more robust loader of multiple songs
    def getPlaylist(self):
        self.playlist = QMediaPlaylist()

    # build out and allow for dirs I could use recursion to make this possible
    def getMusicList(self):
        # this makes a list, gets all files in directory, then makes class with item and adds to list and to fileview
        self.musicList = []
        onlyfiles = [f for f in listdir(self.musicLoc) if isfile(join(self.musicLoc, f))]
        for i, music in enumerate(onlyfiles):
            musicClass = MusicClass.Song(self.musicLoc, music)
            self.musicList.append(musicClass)

            self.addSongToView(musicClass)
# HELPERS
    def addSongToView(self, musicClass):
        min, sec = musicClass.duration
        self.songTableModel.addItem(["", musicClass.artist, musicClass.songName, str(min) + "." + str(sec)])

    # this will be built out later
    def displayErrorMessage(self, error):
        print(error)

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

    def setCurrentSong(self, index):
        self.currentSong = index
        self.songTableModel.setCurrentSong(index)
        print(self.currentSong)

# CONNECTS
    # basically event listeners for changes
    def connects(self):
        self.previous.clicked.connect(self.prevSong)
        self.play.clicked.connect(self.changeSongState)
        self.forward.clicked.connect(self.nextSong)
        self.audioSlider.valueChanged.connect(self.changeAudioVolume)
        self.songSlider.sliderMoved.connect(self.changeSongPosition)
        #self.songSlider.releaseMouse.connect(self.changeSongPosition)
        #self.songSlider.valueChanged.connect(self.changeSongPosition)
        #self.player.positionChanged.connect(self.changeSliderPosition)

        self.fileMenuOpen.triggered.connect(self.getFile)
        self.changeDefaultFolder.triggered.connect(self.getDirectory)

        self.songView.doubleClicked.connect(self.playSongAtIndex)


# FILE THINGIES
    def getFile(self):
        # open dialog, check if user has file, move file to music Folder
        fileInfo = QFileDialog.getOpenFileName(self, 'Open File')
        currentLoc, typeOrSomething = fileInfo
        if currentLoc == '':
            return
        try:
            fileName = currentLoc.split('/')[-1]
            musicClass = MusicClass.Song(self.musicLoc, fileName)
            self.musicList.append(musicClass)
            self.addSongToView(fileName)
        except:
            self.displayErrorMessage("Error: File was not able to be opened.")
            return

        shutil.move(currentLoc, self.musicLoc)

    def getDirectory(self):
        # open dialog, check if user has file, move file to music Folder
        dir = QFileDialog.getExistingDirectory(self, "Select Directory")
        if not dir == '':
            self.musicLoc = dir
            ConfigFunctions.updateConfig(self.volume, dir, configLoc)


# PLAYLIST AND AUDIO PLAYER STUFFS

    def changeAudioVolume(self):
        self.volume = self.audioSlider.value()
        self.player.setVolume(self.volume)
        self.changeSpeakerImg()
        ConfigFunctions.updateConfig(self.volume, self.musicLoc, configLoc)

    # song slider change connects
    # these don't work properly fix later
    def changeSongPosition(self, position):
        self.player.setPosition(position * (self.player.duration() / 100))

    def changeSliderPosition(self, position):
        self.songSlider.setSliderPosition(position / (self.player.duration() / 100))

    # These are basically the same
    # check mediaCount in playlist if > 1 use playlist funcs
    # if not move up current song index and play song at new index
    def nextSong(self):
        print(self.currentSong)
        if self.playlist.mediaCount() > 1:
            self.playlist.next()
        else:
            self.playlist.clear()
            nextSong = self.currentSong + 1
            if nextSong >= len(self.musicList):
                nextSong = 0
            self.setCurrentSong(nextSong)
            self.playlist.addMedia(self.musicList[nextSong].returnMediaContent())
        self.playSong()

    def prevSong(self):
        if self.playlist.mediaCount() > 1:
            self.playlist.previous()
        else:
            self.playlist.clear()
            nextSong = self.currentSong - 1
            if nextSong < 0:
                nextSong = len(self.musicList) - 1
            self.setCurrentSong(nextSong)
            self.playlist.addMedia(self.musicList[nextSong].returnMediaContent())
        self.playSong()

    def playSongAtIndex(self, index):
        # get music list, get MusicClass at row clicked, return MediaContentClass of that index
        songClass = self.musicList[index.row()]
        self.setCurrentSong(index.row())
        song = songClass.returnMediaContent()
        # remove song and add new song then play
        pos = self.playlist.currentIndex()
        self.playlist.removeMedia(pos)
        self.playlist.insertMedia(pos, song)
        self.playSong()


    # This is for the play/pause button
    def changeSongState(self):
        # stop may be added later
        if not self.isPlaying:
            self.playSong()
        elif self.isPlaying:
            self.pauseSong()

    # play song and update the model
    def playSong(self):
        self.player.play()
        self.isPlaying = True
        self.songTableModel.songPlay()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon)

    # play song and update the model
    def pauseSong(self):
        self.player.pause()
        self.isPlaying = False
        self.songTableModel.songPause()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon)

# does stuff
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        win = MainWindow()
        win.show()
        sys.exit(app.exec_())


