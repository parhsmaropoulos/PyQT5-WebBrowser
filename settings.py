from turtle import screensize
from PyQt5.QtWidgets import *

from history import *


class SettingsMenu(QMainWindow):
    def __init__(self, parent):
        super(SettingsMenu, self).__init__(parent)
        self.resize(300, 600)
        self.setWindowTitle('Settings')

        self.listwidget = QListWidget()
        self.listwidget.insertItem(0, "New Tab")
        self.listwidget.insertItem(1, "New Window")
        self.listwidget.insertItem(2, "New Private Window")
        self.listwidget.insertItem(3, "Bookmarks")
        self.listwidget.insertItem(4, "History")
        self.listwidget.insertItem(5, "Print")
        self.listwidget.clicked.connect(lambda item, parent=parent:
                                        self.clicked(item, parent))
        self.setCentralWidget(self.listwidget)

        # Move next to settings btn
        self.move(parent.settings_btn.pos().x() - 330, 0)

    def clicked(self, qmodelindex, parent: QMainWindow):
        item = self.listwidget.currentItem()
        text = item.text()
        if text == 'New Tab':
            parent.tab_open_doubleclick(-1)
        elif text == 'New Window':
            parent.new_window()
        elif text == 'New Private Window':
            parent.new_private_window()
        elif text == 'Bookmarks':
            parent.show_bookmarks()
        elif text == 'History':
            parent.show_history()
        elif text == 'Print':
            parent.print_page()
        self.close()
