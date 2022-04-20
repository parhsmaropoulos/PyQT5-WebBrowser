from db import *


def initBookmarks(self: QMainWindow, parent: QMainWindow):
    bookmarks = getAllBookmarks()
    # Create bookmarks combobox
    # bookmark_combobox = QComboBox()
    # bookmark_combobox.addItems(bookmarks)
    listwidget = QListWidget()
    index = 0
    for book in bookmarks:
        listwidget.insertItem(index, f"{book}")
        index += 1
    listwidget.clicked.connect(
        lambda item: parent.navigate_to_bookmark(listwidget.currentItem().text()))

    return listwidget


def clicked(self, qmodelindex, parent: QMainWindow):
    item = self.listwidget.currentItem()
    text = item.text()
    parent.navigate_to_bookmark(text())


def is_bookmarked(bookmark):
    db_bookmark = getBookmark(bookmark)
    if db_bookmark != "":
        return True
    return False


def resetBookmarksList(bookmark_combobox: QComboBox):
    bookmarks = getAllBookmarks()

    bookmark_combobox.clear()
    bookmark_combobox.addItems(bookmarks)
    return bookmark_combobox


def addBookmark(url):
    QSqlDatabase.database()
    query = QSqlQuery()
    query.exec_(f"insert into bookmarks values('{url}')")
    return


def getAllBookmarks():
    QSqlDatabase.database()
    query = QSqlQuery()
    query.exec_(f"select * from bookmarks")

    bookmark_urls = []
    while query.next():
        bookmark_urls.append(query.value('url'))
    return bookmark_urls


def getBookmark(url):
    QSqlDatabase.database()
    query = QSqlQuery()
    query.exec_(f"select * from bookmarks where url ='{url}'")
    if query.next():
        return query.value('url')
    return ""
