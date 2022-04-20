import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setHostName("localhost")
    db.setDatabaseName("webbrowser.db")
    db.setUserName("user")
    db.setPassword("123")

    if not db.open():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error in Database Creation")
        retval = msg.exec_()
        return False
    query = QSqlQuery()

    query.exec_("create table bookmarks( url varchar(20) UNIQUE);")
    query.exec_(
        "create table history( url varchar(20), time text(40) , UNIQUE(url,time));")
    return True
