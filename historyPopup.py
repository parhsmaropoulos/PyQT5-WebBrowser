from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from history import *


class Popup(QMainWindow):
    def __init__(self, parent):
        super(Popup, self).__init__(parent)
        self.resize(600, 300)
        self.history = initHistory(self, parent)
        self.setWindowTitle('History')
        self.setCentralWidget(self.history)
