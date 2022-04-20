from fbs_runtime.application_context.PyQt5 import ApplicationContext

# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtSql import *
from PyQt5.QtGui import *

import os
import sys
from db import *
from bookmarks import *
from history import *
from tabs import *
from buttons import *
from popup import *
from settings import *


class Window(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        # Establish sqlite connection
        createDB()

        self.mode = 'normal'
        self.settingTabOpen = False
        # creating a tab widget
        self.tabs = initTabs(self)

        # creating a status bar
        self.status = QStatusBar()

        # setting status bar to the main window
        self.setStatusBar(self.status)

        # creating a tool bar for navigation
        navtb = QToolBar("Navigation")

        # adding tool bar tot he main window
        self.addToolBar(navtb)

        # Create buttons
        back_btn = initBackButton(self)
        next_btn = initNextButton(self)
        reload_btn = initReloadButton(self)
        home_btn = initHomeButton(self)

        # Add buttons to navbar
        navtb.addAction(back_btn)
        navtb.addAction(next_btn)
        navtb.addAction(reload_btn)
        navtb.addAction(home_btn)

        # adding a separator
        navtb.addSeparator()

        # creating a line edit widget for URL
        self.urlbar = QLineEdit()

        # adding action to line edit when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # adding line edit to tool bar
        navtb.addWidget(self.urlbar)

        self.star_btn = initStarButton(self)

        navtb.addWidget(self.star_btn)

        self.settings_btn = initSettingsButton(self)
        navtb.addWidget(self.settings_btn)

        # self.bookmarks = getAllBookmarks()

        # creating first tab
        self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')

        # showing all the components
        self.show()

        # setting window title
        self.setWindowTitle("George Browser")

        # opening window in maximized size
        self.showMaximized()
        self.update_star_button()

    # method for adding new tab
    def add_new_tab(self, qurl=None, label="Blank"):

        # if url is blank
        if qurl is None:
            # creating a google url
            qurl = QUrl('http://www.google.com')

        # creating a QWebEngineView object
        browser = QWebEngineView()

        # setting url to browser
        browser.setUrl(qurl)

        # setting tab index
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        # adding action to the browser when url is changed
        # update the url
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        # adding action to the browser when loading is finished
        # set the tab title
        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

    # when double clicked is pressed on tabs
    def tab_open_doubleclick(self, i):

        # checking index i.e
        # No tab under the click
        if i == -1:
            # creating a new tab
            self.add_new_tab()

    # when tab is changed
    def current_tab_changed(self, i):

        # get the curl
        qurl = self.tabs.currentWidget().url()
        # update the url
        self.update_urlbar(qurl, self.tabs.currentWidget())

        # update the title
        self.update_title(self.tabs.currentWidget())

    # when tab is closed
    def close_current_tab(self, i):

        # if there is only one tab
        if self.tabs.count() < 2:
            # do nothing
            return

        # else remove the tab
        self.tabs.removeTab(i)

    # method for updating the title
    def update_title(self, browser):

        # if signal is not from the current tab
        if browser != self.tabs.currentWidget():
            # do nothing
            return

        # get the page title
        title = self.tabs.currentWidget().page().title()

        # set the window title
        self.setWindowTitle("% s" % title)

    # action to go to home
    def navigate_home(self):
        # go to google
        self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))
        self.update_star_button()

    # method for navigate to url
    def navigate_to_url(self):
        # get the line edit text
        # convert it to QUrl object
        q = QUrl(self.urlbar.text())

        # if scheme is blank
        if q.scheme() == "":
            # set scheme
            q.setScheme("http")

        # set the url
        self.tabs.currentWidget().setUrl(q)
        self.update_star_button()

    # method for navigate to url
    def navigate_to_bookmark(self, text):
        q = QUrl(text)

        # if scheme is blank
        if q.scheme() == "":
            # set scheme
            q.setScheme("http")

        # set the url
        self.tabs.currentWidget().setUrl(q)
        self.update_star_button()

    # method to update the url

    def update_urlbar(self, q, browser=None):

        # If this signal is not from the current tab, ignore
        if browser != self.tabs.currentWidget():
            self.update_star_button()
            return
        if self.mode != 'incognito':
            addHistory(q.toString())
        # set text to the url bar
        self.urlbar.setText(q.toString())

        # set cursor position
        self.urlbar.setCursorPosition(0)
        self.update_star_button()

    def save_bookmark(self):
        if self.mode == 'incognito':
            return
        current_url = self.urlbar.text()
        addBookmark(current_url)
        # self.bookmarks = resetBookmarksList(self.bookmarks)
        self.navigate_to_bookmark(current_url)
        return

    def show_history(self):
        if self.mode == 'incognito':
            return
        pop = Popup(self, 'history')
        pop.show()

    def show_bookmarks(self):
        pop = Popup(self, 'bookmarks')
        pop.show()

    def show_settings(self):
        # if self.settingTabOpen == False:
        self.settingTabOpen = True
        self.pop = SettingsMenu(self)
        self.pop.show()

    def close_settings(self):
        self.settingTabOpen = False
        self.pop.close()

    def new_window(self):
        window = Window()

    def new_private_window(self):
        window = IncognitoWindow()

    def print_page(self):
        # Create printer
        printer = QPrinter()
        # Create painter
        painter = QPainter()
        # Start painter
        painter.begin(printer)
        # Grab a widget you want to print
        screen = self.grab()
        # Draw grabbed pixmap
        painter.drawPixmap(10, 10, screen)
        # End painting
        painter.end()

    def update_star_button(self):
        if self.mode == 'incognito':
            return
        already_bookmarked = is_bookmarked(self.urlbar.text())
        if already_bookmarked:
            self.star_btn.setIcon(QIcon(qta.icon('ph.star', color='blue')))
        else:
            self.star_btn.setIcon(QIcon(qta.icon('ph.star')))


class IncognitoWindow(Window):

    # constructor
    def __init__(self, *args, **kwargs):
        super(IncognitoWindow, self).__init__(*args, **kwargs)
        self.setStyleSheet("""
        background-color: hsl(43,43,43);
        color: white;
        """
                           )

        self.mode = 'incognito'

        self.setWindowTitle("George Private Browser")


if __name__ == "__main__":
    # creating a PyQt5 application
    app = QApplication(sys.argv)
    # appctxt = ApplicationContext()

    # setting name to the application
    # appctxt.app.setApplicationName("Custom Web Browser")
    app.setApplicationName("Custom Web Browser")
    # creating MainWindow object
    window = Window()

    # loop
    app.exec_()
    # sys.exit(appctxt.app.exec())
