import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc


class TableView(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super(TableView, self).__init__(*args, **kwargs)
        self.songs = []
        self.columnCount = 3
        self.speakerRow = 2
        # change this whenver or make it an array and have another var
        self.speakerImage = ":/icons/speaker-max.png"


    def rowCount(self, index):
        return len(self.songs)

    def columnCount(self, index):
        return self.columnCount

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.songs[index.row()][index.column()]
            return text

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        #print(section, orientation)
        if orientation == Qt.Vertical:
            if role == Qt.DecorationRole:
                if section == self.speakerRow:
                    test = QtGui.QPixmap(self.speakerImage)
                    test = test.scaled(15,15)
                    return test
                return ""
            if role == Qt.DisplayRole:
                return ""
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return ""
        return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout(window)

myTableWidget = QtWidgets.QTableView()
model = TableView()

layout.addWidget(myTableWidget)
window.show()


yee = myTableWidget.verticalHeader()
print(yee)
#myTableWidget.header

#myTableWidget.verticalHeader().hide()
#myTableWidget.horizontalHeader().hide()
myTableWidget.setShowGrid(False)
myTableWidget.setFocusPolicy(Qt.NoFocus)
myTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
#myTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.set))
myTableWidget.setStyleSheet("color: rgb(230, 230, 230); alternate-background-color:rgb(36, 36, 36); background-color:rgb(28,28,28); border:none; selection-background-color: rgb(70,70,70);} QHeaderView::section { background-color:rgb(36, 36, 36);")


iconsByState = [":/icons/speaker-none.png", ":/icons/speaker-max.png", ""]
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap(":/icons/speaker-max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

label = QtWidgets.QLabel()
label.setMaximumSize(15, 15)
label.setScaledContents(True)
label.setPixmap(QtGui.QPixmap(":/icons/speaker-max.png"))
label.setStyleSheet("border:none; padding: 0; margin: 0;")
#myTableWidget.clicked.connect(newClickFunc)

myTableWidget.setAlternatingRowColors(True)

model.songs.append(["123", "dude", "hi3", "h3"])
model.songs.append(["hi2", "hi3", "h3", "cool"])
model.songs.append(["hi2", "hi3", "h3", "cool"])
model.layoutChanged.emit()

model.setHeaderData(1, Qt.Vertical, "askldfasdklfjasdkljfaklsdfjklasdfjklasdjklasdjklasdjklasdfkljasdfljk")
model.headerDataChanged.emit(Qt.Vertical,0,2)
model.headerDataChanged.emit(Qt.Horizontal,0,2)
#print(model.headerData(1, Qt.Vertical))
myTableWidget.setModel(model)

#model.speakerRow = 1
model.speakerImage = ":/icons/speaker-none.png"

myTableWidget.resizeRowsToContents()

model.layoutChanged.emit()

sys.exit(app.exec_())