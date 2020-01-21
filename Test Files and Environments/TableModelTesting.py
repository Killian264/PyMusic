import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc

# this should be be changed so that it can take any number of columns and headers
class TableView(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super(TableView, self).__init__(*args, **kwargs)
        self.songs = []
        self.headers = ["", "Artist", "Song", "Length"]
        self.columnCount = 4
        self.currentSong = 1
        # change this whenver or make it an array and have another var
        self.speakerImage = ":/icons/speaker-max.png"


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
            # This should be moved out of this into global or inside some kind of dictionary for pixmaps
            # I have heard of some kind of pixmap like holder class <- check that out
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/speaker-max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            if index.row() == self.currentSong and index.column() == 0:
                return icon
        # for alignment specifications
        if role == Qt.TextAlignmentRole:
            # align right for length which is final column
            if index.column() == self.columnCount - 1:
                return Qt.AlignRight | Qt.AlignVCenter

    # set length to be right aligned
    def headerData(self, index, orientation, role):
        # orientation check shouldnt be nesiccary with vertical disabled but I will keep for now
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[index]


# boring init stuff
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout(window)

myTableWidget = QtWidgets.QTableView()
model = TableView()

layout.addWidget(myTableWidget)
window.show()

# important code snippet for later
'''
https://stackoverflow.com/questions/5927499/how-to-get-selected-rows-in-qtableview
QModelIndexList selection = yourTableView->selectionModel()->selectedRows();

// Multiple rows can be selected
for(int i=0; i< selection.count(); i++)
{
    QModelIndex index = selection.at(i);
    qDebug() << index.row();
}
'''


# bet you cant guess what this does
myTableWidget.verticalHeader().hide()
#myTableWidget.horizontalHeader().hide()


myTableWidget.setShowGrid(False)

# removes cell focus
myTableWidget.setFocusPolicy(Qt.NoFocus)
# makes focus all items
myTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

# fix this monstrosity
#myTableWidget.setStyleSheet("color: rgb(230, 230, 230); alternate-background-color:rgb(36, 36, 36); background-color:rgb(28,28,28); border:none; selection-background-color: rgb(70,70,70);} QHeaderView::section { background-color:rgb(36, 36, 36);")
myTableWidget.setStyleSheet("color: rgb(230, 230, 230); alternate-background-color:rgb(36, 36, 36); background-color:rgb(28,28,28); border:none; selection-background-color: rgb(70,70,70);} QHeaderView::section { background-color:rgb(36, 36, 36); }")


# very important
myTableWidget.setAlternatingRowColors(True)

# this is how data is added, this could be overloaded to allow for easy transitions between column amounts with some witchcraft inside of the model
# or not idk how that would look/be
model.songs.append(["", "Cool artist dood", "Super duper long super string of song name thats long", "2.25"])
model.songs.append(["", "hi3", "h3", "cool"])
model.songs.append(["", "hi3", "h3", "cool"])
# do this when data is changed inside of the double data array
model.layoutChanged.emit()

# essential set model
myTableWidget.setModel(model)

# changes rows to fit column content
#myTableWidget.resizeRowsToContents()

# row sizing is important for fixed headerview
myTableWidget.setColumnWidth(0, 1)
myTableWidget.setColumnWidth(1, 150)
myTableWidget.setColumnWidth(2, 300)
myTableWidget.setColumnWidth(3, 50)

# header and views, setting 2 to stretch and 1 to nothing  allows for resizing while keeping the benefits of a constant size
# note if I allow model to have many columns this would need to be passed or changed
header = myTableWidget.horizontalHeader()
header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
#header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)

verticalHeader = myTableWidget.verticalHeader()

verticalHeader.setDefaultSectionSize(1);

sys.exit(app.exec_())