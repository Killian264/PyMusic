from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(913, 642)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet("background-color: rgb(36,36,36);\n""color: white;")
        self.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.songView = QtWidgets.QListView(self.centralwidget)
        self.songView.setObjectName("songView")
        self.verticalLayout.addWidget(self.songView)
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
        self.songProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songProgressBar.sizePolicy().hasHeightForWidth())
        # Progress bar
        self.songProgressBar.setSizePolicy(sizePolicy)
        self.songProgressBar.setMaximumSize(QtCore.QSize(16777215, 2))
        self.songProgressBar.setStyleSheet("QProgressBar::chunk { background: black; }")
        self.songProgressBar.setProperty("value", 24)
        self.songProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.songProgressBar.setFormat("")
        self.songProgressBar.setObjectName("songProgressBar")
        self.horizontalLayout.addWidget(self.songProgressBar)

        self.speakerImage = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speakerImage.sizePolicy().hasHeightForWidth())
        # speaker image label
        self.speakerImage.setSizePolicy(sizePolicy)
        self.speakerImage.setMaximumSize(QtCore.QSize(20, 20))
        self.speakerImage.setText("")
        self.speakerImage.setPixmap(QtGui.QPixmap(":/icons/speaker.png"))
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

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "PyMusic"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.fileMenuOpen.setText(_translate("MainWindow", "Open"))
        self.changeDefaultFolder.setText(_translate("MainWindow", "Change Music Folder"))

def PlaySong():
        print("hello this is test")
        playlist = QMediaPlaylist()
        url = QtCore.QUrl.fromLocalFile("./Music/song.mp3")
        playlist.addMedia(QMediaContent(url))
        playlist.setPlaybackMode(QMediaPlaylist.Loop)

        player = QMediaPlayer()
        player.setPlaylist(playlist)
        player.play()
        print("hello this is another test")

if __name__ == "__main__":
        PlaySong()

        app = QtWidgets.QApplication(sys.argv)
        win = MainWindow()
        win.show()
        sys.exit(app.exec_())


