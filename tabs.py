from PyQt5.QtWidgets import *


def initTabs(self: QMainWindow):
    tabs = QTabWidget()

    # making document mode true
    tabs.setDocumentMode(True)

    # adding action when double clicked
    tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

    # adding action when tab is changed
    tabs.currentChanged.connect(self.current_tab_changed)

    # making tabs closeable
    tabs.setTabsClosable(True)

    # adding action when tab close is requested
    tabs.tabCloseRequested.connect(self.close_current_tab)

    # making tabs as central widget
    self.setCentralWidget(tabs)

    return tabs
