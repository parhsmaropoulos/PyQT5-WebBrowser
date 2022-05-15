from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from history import *
from bookmarks import *
from buttons import *


class Popup(QMainWindow):
    def __init__(self, parent, type):
        super(Popup, self).__init__(parent)
        if type == 'history':
            self.resize(600, 300)
            self.history = initHistory(self, parent)
            self.setWindowTitle('History')
            optionsTab = QToolBar("Navigation")
            # adding tool bar
            self.addToolBar(optionsTab)

            delete_today_history_button = initDeleteTodayHistoryButton(parent)
            delete_month_history_button = initDeleteMonthHistoryButton(parent)
            clear_history_button = initClearHistoryButton(parent)

            optionsTab.addWidget(delete_today_history_button)
            optionsTab.addWidget(delete_month_history_button)
            optionsTab.addWidget(clear_history_button)

            self.setCentralWidget(self.history)
        elif type == 'bookmarks':
            self.resize(300, 600)
            self.bookmarks = initBookmarks(self, parent)
            self.setWindowTitle('Bookmarks')
            self.setCentralWidget(self.bookmarks)
            self.move(parent.settings_btn.pos().x() - 330, 0)
