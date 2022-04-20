from asyncio.windows_events import NULL
import pprint
from db import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
from datetime import date

import qtawesome as qta


class ListWidget(QListWidget):
    def clicked(self, item):
        QMessageBox.information(
            self, "ListWidget", "ListWidget: " + item.text())


def initHistory(self: QMainWindow, parent: QMainWindow):
    history = getHistory()
    # Create bookmarks combobox
    history_table = QTableWidget()
    history_table.setRowCount(len(history))
    history_table.setColumnCount(3)
    header = history_table.horizontalHeader()
    header.setSectionResizeMode(0, QHeaderView.Stretch)
    header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
    header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
    index = 0
    # First date
    date = history[0][1].strip()
    for hist in history:
        # Check if date changes
        if hist[1].strip() != date:
            history_table.insertRow(index)
            history_table.setItem(
                index, 0, QTableWidgetItem(f"{hist[1].strip()}"))
            history_table.item(index, 0).setFlags(
                history_table.item(index, 0).flags() & ~Qt.ItemIsEnabled & ~Qt.ItemIsEditable & Qt.ItemIsSelectable)
            history_table.setItem(index, 1, QTableWidgetItem(""))
            index += 1
        history_table.setItem(
            index, 0, QTableWidgetItem(f"{hist[0].strip()}"))
        history_table.setItem(
            index, 1, QTableWidgetItem(f"{hist[1].strip()}"))
        history_table.setItem(
            index, 2, QTableWidgetItem("X"))
        date = hist[1].strip()
        index += 1
    history_table.move(0, 0)
    history_table.itemClicked.connect(
        lambda x, parent=parent, table=history_table: item_clicked(x, parent, table))
    history_table.itemClicked.connect(
        lambda x:   self.close() if history_table.item(
            x.row(), 1).text() != ""else NULL
    )
    return history_table


def item_clicked(item, parent, table):
    row = item.row()
    col = item.row()
    text = item.text().strip()
    # Navigate
    if col == 1:
        if text != "":
            parent.navigate_to_bookmark(text)
    # Date = nothing
    elif col == 2:
        return
    # Delete
    else:
        url = table.item(row, 0).text()
        date = table.item(row, 1).text()
        deleteHistory(url, date)
    return


def addHistory(url):
    today = date.today()
    today_format = today.strftime("%d-%m-%Y")
    QSqlDatabase.database()
    query = QSqlQuery()
    query.exec_(f"insert into history values('{url}', '{today_format}')")
    return


def deleteHistory(url, date):
    QSqlDatabase.database()
    query = QSqlQuery()
    print(url)
    print(date)
    query.exec_(f"delete from history where url ='{url}' and time='{date}'")
    return


def getHistory():
    QSqlDatabase.database()
    query = QSqlQuery()
    query.exec_(f"select url,time from history")

    history = []
    while query.next():
        history.append([query.value(0), query.value(1)])
    return history
