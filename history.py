from db import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime


class ListWidget(QListWidget):
    def clicked(self, item):
        QMessageBox.information(
            self, "ListWidget", "ListWidget: " + item.text())


def initHistory(self: QMainWindow, parent: QMainWindow):
    history = getHistory()
    # Create bookmarks combobox
    history_table = QTableWidget()
    history_table.setRowCount(len(history) + 1)
    history_table.setColumnCount(4)
    history_table.setItem(0, 0, QTableWidgetItem("Url"))
    history_table.setItem(0, 1, QTableWidgetItem("Time"))
    # history_table.setItem(0, 2, QTableWidgetItem("Go to"))
    # history_table.setItem(0, 3, QTableWidgetItem("Remove"))
    index = 1
    for hist in history:
        splited = hist.split("-")
        history_table.setItem(
            index, 0, QTableWidgetItem(f"{splited[0].strip()}"))
        history_table.setItem(
            index, 1, QTableWidgetItem(f"{splited[1].strip()}"))
        history_table.setItem(index, 2, QTableWidgetItem("Go to"))
        history_table.setItem(index, 3, QTableWidgetItem("Remove"))

        index += 1
    history_table.move(0, 0)
    # history_list = ListWidget()
    # history_list.resize(300, 120)
    # history_list.addItems(history)
    # history_list.itemDoubleClicked.connect(
    #     lambda x: parent.navigate_to_bookmark(x.text().split("-")[0].strip()))
    # history_list.itemDoubleClicked.connect(self.close)
    history_table.itemClicked.connect(
        lambda x:  parent.navigate_to_bookmark(history[x.row()-1].split("-")[0].strip()))
    return history_table


def addHistory(url):
    timeStamp = datetime.now()
    QSqlDatabase.database()
    query = QSqlQuery()
    query.exec_(f"insert into history values('{url}', '{timeStamp}')")
    return


def getHistory():
    QSqlDatabase.database()
    query = QSqlQuery()
    query.exec_(f"select url,datetime(time) as time from history")

    history = []
    while query.next():
        history.append(f"{ query.value('url') }  - { query.value('time') }")
    return history
