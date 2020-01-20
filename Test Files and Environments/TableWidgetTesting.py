import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc


class TableView(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super(TableView, self).__init__(*args, **kwargs)
        self.songs = []
        self.columnCount = 4

    def rowCount(self, index):
        return len(self.songs)

    def columnCount(self, index):
        return self.columnCount

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.songs[index.row()][index.column()]
            return text




app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout(window)

testTable = QtWidgets.QTableView()
model = TableView()
testTable.setModel(model)

myTableWidget = QtWidgets.QTableWidget()
myTableWidget.setRowCount(5)
myTableWidget.setColumnCount(3)

myTableWidget.verticalHeader().hide()
myTableWidget.horizontalHeader().hide()

myTableWidget.setColumnWidth(0, 1)

myTableWidget.verticalHeader().setDefaultSectionSize(3)

myTableWidget.setShowGrid(False)

myTableWidget.setFocusPolicy(Qt.NoFocus)

myTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)

#myTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.set))

myTableWidget.setStyleSheet("color: rgb(230, 230, 230); alternate-background-color:rgb(36, 36, 36); background-color:rgb(28,28,28); border:none; selection-background-color: rgb(70,70,70);")

def testfunc(iRow, iColumn):
    print("hello")
    print(iRow, iColumn)
    myTableWidget.clearSelection()
    myTableWidget.setRangeSelected(QtWidgets.QTableWidgetSelectionRange(iRow,0,iRow,myTableWidget.columnCount() - 1), True)
    myTableWidget.setRowCount(100)


iconsByState = [":/icons/speaker-none.png", ":/icons/speaker-max.png", ""]
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap(":/icons/speaker-max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)



widgetitem = myTableWidget.itemAt(1,1)
print(widgetitem)

myTableWidget.cellClicked.connect(testfunc)

myTableWidget.setAlternatingRowColors(True)

for column in range(myTableWidget.columnCount()):
    for row in range(myTableWidget.rowCount()):
        if column == 0:
            widget = QtWidgets.QWidget()
            label = QtWidgets.QLabel()
            label.setMaximumSize(15, 15)
            label.setScaledContents(True)
            label.setPixmap(QtGui.QPixmap(":/icons/speaker-max.png"))
            label.setStyleSheet("border:none; padding: 0; margin: 0;")
            pLayout = QtWidgets.QHBoxLayout(widget)
            pLayout.addWidget(label)
            pLayout.setAlignment(Qt.AlignCenter)
            pLayout.setContentsMargins(0, 0, 0, 0)
            widget.setLayout(pLayout)
            myTableWidget.setCellWidget(row, column, widget)


        else:
            myTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem("H"))


myTableWidget.resizeColumnToContents(0)



layout.addWidget(myTableWidget)
layout.addWidget(testTable)
window.show()

model.songs.append(["hi", "hi2", "hi3", "h3"])
model.layoutChanged.emit()

sys.exit(app.exec_())


for i in range(1,5):
    pass