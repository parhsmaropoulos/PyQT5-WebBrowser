from db import *


def initBookmarks():
    bookmarks = getAllBookmarks()
    # Create bookmarks combobox
    bookmark_combobox = QComboBox()
    bookmark_combobox.addItems(bookmarks)
    return bookmark_combobox


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
