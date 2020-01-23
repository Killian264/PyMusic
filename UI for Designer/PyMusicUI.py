# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyMusic.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1134, 749)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(36,36,36);\n"
"color: white;")
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(2, 0, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.setContentsMargins(-1, 0, -1, -1)
        self.mainLayout.setHorizontalSpacing(0)
        self.mainLayout.setVerticalSpacing(4)
        self.mainLayout.setObjectName("mainLayout")
        self.songQueueView = QtWidgets.QListView(self.centralwidget)
        self.songQueueView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songQueueView.sizePolicy().hasHeightForWidth())
        self.songQueueView.setSizePolicy(sizePolicy)
        self.songQueueView.setMinimumSize(QtCore.QSize(0, 0))
        self.songQueueView.setMaximumSize(QtCore.QSize(220, 16777215))
        self.songQueueView.setStyleSheet("")
        self.songQueueView.setObjectName("songQueueView")
        self.mainLayout.addWidget(self.songQueueView, 0, 2, 1, 1)
        self.songTableView = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.songTableView.setFont(font)
        self.songTableView.setStyleSheet("")
        self.songTableView.setObjectName("songTableView")
        self.mainLayout.addWidget(self.songTableView, 0, 1, 1, 1)
        self.playlistView = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlistView.sizePolicy().hasHeightForWidth())
        self.playlistView.setSizePolicy(sizePolicy)
        self.playlistView.setMaximumSize(QtCore.QSize(200, 16777215))
        self.playlistView.setObjectName("playlistView")
        self.mainLayout.addWidget(self.playlistView, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(10, 4, 10, 4)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previousBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousBtn.sizePolicy().hasHeightForWidth())
        self.previousBtn.setSizePolicy(sizePolicy)
        self.previousBtn.setStyleSheet("border: none;")
        self.previousBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousBtn.setIcon(icon)
        self.previousBtn.setObjectName("previousBtn")
        self.horizontalLayout.addWidget(self.previousBtn)
        self.playBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playBtn.sizePolicy().hasHeightForWidth())
        self.playBtn.setSizePolicy(sizePolicy)
        self.playBtn.setMinimumSize(QtCore.QSize(40, 30))
        self.playBtn.setStyleSheet("border: none;")
        self.playBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playBtn.setIcon(icon1)
        self.playBtn.setIconSize(QtCore.QSize(25, 24))
        self.playBtn.setObjectName("playBtn")
        self.horizontalLayout.addWidget(self.playBtn)
        self.forwardBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forwardBtn.sizePolicy().hasHeightForWidth())
        self.forwardBtn.setSizePolicy(sizePolicy)
        self.forwardBtn.setStyleSheet("border: none;")
        self.forwardBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forwardBtn.setIcon(icon2)
        self.forwardBtn.setObjectName("forwardBtn")
        self.horizontalLayout.addWidget(self.forwardBtn)
        spacerItem = QtWidgets.QSpacerItem(30, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.songSliderLayout = QtWidgets.QVBoxLayout()
        self.songSliderLayout.setSpacing(0)
        self.songSliderLayout.setObjectName("songSliderLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.songInformationLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.songInformationLabel.setFont(font)
        self.songInformationLabel.setObjectName("songInformationLabel")
        self.horizontalLayout_2.addWidget(self.songInformationLabel)
        self.songNameLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.songNameLabel.setFont(font)
        self.songNameLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.songNameLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.songNameLabel.setObjectName("songNameLabel")
        self.horizontalLayout_2.addWidget(self.songNameLabel)
        self.songLengthLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.songLengthLabel.setFont(font)
        self.songLengthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.songLengthLabel.setObjectName("songLengthLabel")
        self.horizontalLayout_2.addWidget(self.songLengthLabel)
        self.songSliderLayout.addLayout(self.horizontalLayout_2)
        self.songSlider = QtWidgets.QSlider(self.widget)
        self.songSlider.setMinimumSize(QtCore.QSize(0, 15))
        self.songSlider.setStyleSheet(".QSlider {\n"
"    min-height: 15px;\n"
"    max-height: 15px;\n"
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
        self.songSlider.setObjectName("songSlider")
        self.songSliderLayout.addWidget(self.songSlider)
        self.horizontalLayout.addLayout(self.songSliderLayout)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.speakerImageLabel = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speakerImageLabel.sizePolicy().hasHeightForWidth())
        self.speakerImageLabel.setSizePolicy(sizePolicy)
        self.speakerImageLabel.setMaximumSize(QtCore.QSize(20, 20))
        self.speakerImageLabel.setText("")
        self.speakerImageLabel.setPixmap(QtGui.QPixmap(":/icons/speaker-max.png"))
        self.speakerImageLabel.setScaledContents(True)
        self.speakerImageLabel.setObjectName("speakerImageLabel")
        self.horizontalLayout.addWidget(self.speakerImageLabel)
        self.audioSlider = QtWidgets.QSlider(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioSlider.sizePolicy().hasHeightForWidth())
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
        self.mainLayout.addWidget(self.widget, 1, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1134, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPlayback = QtWidgets.QMenu(self.menubar)
        self.menuPlayback.setObjectName("menuPlayback")
        MainWindow.setMenuBar(self.menubar)
        self.fileMenuOpen = QtWidgets.QAction(MainWindow)
        self.fileMenuOpen.setObjectName("fileMenuOpen")
        self.changeDefaultFolder = QtWidgets.QAction(MainWindow)
        self.changeDefaultFolder.setObjectName("changeDefaultFolder")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionPause = QtWidgets.QAction(MainWindow)
        self.actionPause.setObjectName("actionPause")
        self.actionStop_2 = QtWidgets.QAction(MainWindow)
        self.actionStop_2.setObjectName("actionStop_2")
        self.actionPrevioux = QtWidgets.QAction(MainWindow)
        self.actionPrevioux.setObjectName("actionPrevioux")
        self.actionNext = QtWidgets.QAction(MainWindow)
        self.actionNext.setObjectName("actionNext")
        self.actionRandom = QtWidgets.QAction(MainWindow)
        self.actionRandom.setObjectName("actionRandom")
        self.actionPlay_for_specified_time = QtWidgets.QAction(MainWindow)
        self.actionPlay_for_specified_time.setObjectName("actionPlay_for_specified_time")
        self.menuFile.addAction(self.fileMenuOpen)
        self.menuFile.addAction(self.changeDefaultFolder)
        self.menuFile.addAction(self.actionExit)
        self.menuPlayback.addAction(self.actionStop)
        self.menuPlayback.addAction(self.actionPause)
        self.menuPlayback.addAction(self.actionStop_2)
        self.menuPlayback.addAction(self.actionPrevioux)
        self.menuPlayback.addAction(self.actionNext)
        self.menuPlayback.addSeparator()
        self.menuPlayback.addAction(self.actionRandom)
        self.menuPlayback.addAction(self.actionPlay_for_specified_time)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPlayback.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyMusic"))
        self.songInformationLabel.setText(_translate("MainWindow", "Song Information"))
        self.songNameLabel.setText(_translate("MainWindow", "No Regrets ft. Krewella (Hopex Remix)"))
        self.songLengthLabel.setText(_translate("MainWindow", "0:01/3:21"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPlayback.setTitle(_translate("MainWindow", "Playback"))
        self.fileMenuOpen.setText(_translate("MainWindow", "Open"))
        self.changeDefaultFolder.setText(_translate("MainWindow", "Change Music Folder"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionStop.setText(_translate("MainWindow", "Play"))
        self.actionPause.setText(_translate("MainWindow", "Pause"))
        self.actionStop_2.setText(_translate("MainWindow", "Stop"))
        self.actionPrevioux.setText(_translate("MainWindow", "Previous"))
        self.actionNext.setText(_translate("MainWindow", "Next"))
        self.actionRandom.setText(_translate("MainWindow", "Random Playback Here"))
        self.actionPlay_for_specified_time.setText(_translate("MainWindow", "Play for specified time"))
import icons_rc