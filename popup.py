from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from history import *
from bookmarks import *


class Popup(QMainWindow):
    def __init__(self, parent, type):
        super(Popup, self).__init__(parent)
        if type == 'history':
            self.resize(600, 300)
            self.history = initHistory(self, parent)
            self.setWindowTitle('History')
            self.setCentralWidget(self.history)
        elif type == 'bookmarks':
            self.resize(300, 600)
            self.bookmarks = initBookmarks(self, parent)
            self.setWindowTitle('Bookmarks')
            self.setCentralWidget(self.bookmarks)
            self.move(parent.settings_btn.pos().x() - 330, 0)
