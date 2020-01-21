from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
import icons_rc

# this should be be changed so that it can take any number of columns and headers
class SongTableModel(QtCore.QAbstractTableModel):
    def __init__(self, columnCount, headers, songs=None,  *args, **kwargs):
        super(SongTableModel, self).__init__(*args, **kwargs)
        # this should be a double array of song data
        self.songs = songs or []
        # headers is list of strings like so: ["", "Artist", "Song", "Length"]
        self.headers = headers
        self.columnCount = columnCount
        # index of current song
        self.currentSong = -1

        # -1 = not playing, 0 = paused, 1 = playing
        self.songState = -1

        self.setupIcon()

    def addItem(self, songInfoList):
        self.songs.append(songInfoList)

    def setupIcon(self):
        # I have heard of some kind of pixmap like holder class <- check that out
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/speaker-max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconPlaying = icon

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/speaker-none.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconPaused = icon

    def setCurrentSong(self, songIndex):
        self.currentSong = songIndex
        self.layoutChanged.emit()

    def songPlay(self):
        self.songState = 1
        self.layoutChanged.emit()

    def songPause(self):
        self.songState = 0
        self.layoutChanged.emit()

    def songStop(self):
        self.songState = -1
        self.layoutChanged.emit()

    # STUFF FOR INHERITANCE
    def rowCount(self, index):
        return len(self.songs)

    def columnCount(self, index):
        return self.columnCount

    def data(self, index, role):
        # for data
        if role == Qt.DisplayRole:
            text = self.songs[index.row()][index.column()]
            return text
        # for decoration like pixmap
        if role == Qt.DecorationRole:
            if index.row() == self.currentSong and index.column() == 0 and self.songState != -1:
                return self.iconPlaying if self.songState == 1 else self.iconPaused
        # for alignment specifications
        if role == Qt.TextAlignmentRole:
            # align right for length which is final column
            if index.column() == self.columnCount - 1:
                return Qt.AlignRight | Qt.AlignVCenter

    def headerData(self, index, orientation, role):
        # orientation check shouldn't be necessary with vertical disabled but I will keep for now
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[index]
        if role == Qt.TextAlignmentRole and orientation == Qt.Horizontal:
                return Qt.AlignVCenter