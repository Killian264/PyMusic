from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import TableViewModel
import icons_rc

def setupUi(UI):
    UI.setObjectName("MainWindow")
    UI.resize(913, 642)

    # size policy
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(UI.sizePolicy().hasHeightForWidth())
    UI.setSizePolicy(sizePolicy)
    UI.setStyleSheet("background-color: rgb(36,36,36);\n""color: white;")
    # UI.setStyleSheet("background-color: rgb(36,36,36);\n")
    UI.setDocumentMode(True)

    # some layouts
    UI.centralwidget = QtWidgets.QWidget(UI)
    UI.centralwidget.setObjectName("centralwidget")

    UI.verticalLayout_2 = QtWidgets.QVBoxLayout(UI.centralwidget)
    UI.verticalLayout_2.setContentsMargins(-1, 0, -1, 6)
    UI.verticalLayout_2.setObjectName("verticalLayout_2")

    UI.verticalLayout = QtWidgets.QVBoxLayout()
    UI.verticalLayout.setSpacing(6)
    UI.verticalLayout.setObjectName("verticalLayout")

    # INIT -- SongView
    UI.songView = QtWidgets.QTableView(UI.centralwidget)
    UI.songView.setObjectName("songView")
    UI.songTableModel = TableViewModel.SongTableModel(columnCount=4, headers=["", "Artist", "Song", "Length"])
    UI.songView.setModel(UI.songTableModel)
    UI.verticalLayout.addWidget(UI.songView)

    # base size and resizing modes
    UI.songView.setColumnWidth(0, 1)
    UI.songView.setColumnWidth(1, 150)
    UI.songView.setColumnWidth(2, 300)
    UI.songView.setColumnWidth(3, 50)
    # header and views, setting 2 to stretch and 1 to nothing  allows for resizing while keeping the benefits of a constant size
    # note if I allow model to have many columns this would need to be passed or changed
    header = UI.songView.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
    # header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)

    # FOCUS -- SongView
    # removes cell focus
    UI.songView.setFocusPolicy(Qt.NoFocus)
    # makes focus all items
    UI.songView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    # VISUAL DESIGN -- SongView
    UI.songView.verticalHeader().hide()
    UI.songView.setShowGrid(False)
    UI.songView.setAlternatingRowColors(True)

    # minimizes the vertical header size
    verticalHeader = UI.songView.verticalHeader()
    verticalHeader.setDefaultSectionSize(1);
    # minimize size of top column
    horizontalHeader = UI.songView.horizontalHeader()
    horizontalHeader.setFixedHeight(21)
    horizontalHeader.setStyleSheet(
        """color:black; background-color: rgb(28, 28, 28); alternate-background-color: rgb(36, 36, 36); """)
    UI.songView.setStyleSheet("""
        color: rgb(230, 230, 230);
        alternate-background-color:rgb(36, 36, 36);
        background-color:rgb(28,28,28);
        border:none;
        selection-background-color: rgb(70,70,70);
        QHeaderView::section { background-color:rgb(36, 36, 36); }"""
                                )

    # END -- SongView

    # previous button
    UI.horizontalLayout = QtWidgets.QHBoxLayout()
    UI.horizontalLayout.setSpacing(6)
    UI.horizontalLayout.setObjectName("horizontalLayout")
    UI.previous = QtWidgets.QPushButton(UI.centralwidget)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(UI.previous.sizePolicy().hasHeightForWidth())
    UI.previous.setSizePolicy(sizePolicy)
    UI.previous.setStyleSheet("background-color: rgb(36,36,36);\n""border: none;")
    UI.previous.setText("")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/icons/Previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    UI.previous.setIcon(icon)
    UI.previous.setObjectName("previous")
    UI.horizontalLayout.addWidget(UI.previous)

    # play button
    UI.play = QtWidgets.QPushButton(UI.centralwidget)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(UI.play.sizePolicy().hasHeightForWidth())
    UI.play.setSizePolicy(sizePolicy)
    UI.play.setMinimumSize(QtCore.QSize(40, 30))
    UI.play.setStyleSheet("border: none;")
    UI.play.setText("")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(":/icons/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    UI.play.setIcon(icon1)
    UI.play.setIconSize(QtCore.QSize(25, 24))
    UI.play.setObjectName("play")
    UI.horizontalLayout.addWidget(UI.play)

    # forward button
    UI.forward = QtWidgets.QPushButton(UI.centralwidget)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(UI.forward.sizePolicy().hasHeightForWidth())
    UI.forward.setSizePolicy(sizePolicy)
    UI.forward.setStyleSheet("border: none;")
    UI.forward.setText("")
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(":/icons/Next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    UI.forward.setIcon(icon2)
    UI.forward.setObjectName("forward")
    UI.horizontalLayout.addWidget(UI.forward)

    # song progress slider
    # CustomSlider.Slider
    # QtWidgets.QSlider
    UI.songSlider = QtWidgets.QSlider(UI.centralwidget)
    # UI.songSlider = CustomSlider.Slider(UI.centralwidget)
    UI.songSlider.setStyleSheet(".QSlider {\n"
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
    UI.songSlider.setOrientation(QtCore.Qt.Horizontal)
    UI.songSlider.setObjectName("horizontalSlider")
    UI.horizontalLayout.addWidget(UI.songSlider)

    # speaker image label
    UI.speakerImage = QtWidgets.QLabel(UI.centralwidget)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(UI.speakerImage.sizePolicy().hasHeightForWidth())
    UI.speakerImage.setSizePolicy(sizePolicy)
    UI.speakerImage.setMaximumSize(QtCore.QSize(20, 20))
    UI.speakerImage.setText("")
    UI.speakerImage.setPixmap(QtGui.QPixmap(":/icons/speaker-max.png"))
    UI.speakerImage.setScaledContents(True)
    UI.speakerImage.setObjectName("speakerImage")
    UI.horizontalLayout.addWidget(UI.speakerImage)
    UI.audioSlider = QtWidgets.QSlider(UI.centralwidget)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(UI.audioSlider.sizePolicy().hasHeightForWidth())

    # Audio Slider
    UI.audioSlider.setSizePolicy(sizePolicy)
    UI.audioSlider.setStyleSheet(".QSlider {\n"
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
    UI.audioSlider.setOrientation(QtCore.Qt.Horizontal)
    UI.audioSlider.setObjectName("audioSlider")
    UI.horizontalLayout.addWidget(UI.audioSlider)
    UI.verticalLayout.addLayout(UI.horizontalLayout)
    UI.verticalLayout_2.addLayout(UI.verticalLayout)
    UI.setCentralWidget(UI.centralwidget)

    # menubar
    UI.menubar = QtWidgets.QMenuBar(UI)
    UI.menubar.setGeometry(QtCore.QRect(0, 0, 913, 21))
    UI.menubar.setObjectName("menubar")
    UI.menuFile = QtWidgets.QMenu(UI.menubar)
    UI.menuFile.setObjectName("menuFile")
    UI.setMenuBar(UI.menubar)
    UI.fileMenuOpen = QtWidgets.QAction(UI)
    UI.fileMenuOpen.setObjectName("fileMenuOpen")
    UI.changeDefaultFolder = QtWidgets.QAction(UI)
    UI.changeDefaultFolder.setObjectName("changeDefaultFolder")
    UI.menuFile.addAction(UI.fileMenuOpen)
    UI.menuFile.addAction(UI.changeDefaultFolder)
    UI.menubar.addAction(UI.menuFile.menuAction())

    # not sure why retranslateUi is split up
    retranslateUi(UI)
    QtCore.QMetaObject.connectSlotsByName(UI)

def retranslateUi(UI):
    _translate = QtCore.QCoreApplication.translate
    UI.setWindowTitle(_translate("MainWindow", "PyMusic"))
    UI.menuFile.setTitle(_translate("MainWindow", "File"))
    UI.fileMenuOpen.setText(_translate("MainWindow", "Open Music File"))
    UI.changeDefaultFolder.setText(_translate("MainWindow", "Change Music Folder"))