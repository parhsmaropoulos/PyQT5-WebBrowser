from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def initBackButton(self: QMainWindow):
    back_btn = QAction("Back", self)
    back_btn.setStatusTip("Back to previous page")
    back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

    return back_btn


def initNextButton(self: QMainWindow):
    next_btn = QAction("Forward", self)
    next_btn.setStatusTip("Forward to next page")
    next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
    return next_btn


def initBackButton(self: QMainWindow):
    back_btn = QAction("Back", self)
    back_btn.setStatusTip("Back to previous page")
    back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

    return back_btn


def initReloadButton(self: QMainWindow):
    reload_btn = QAction("Reload", self)
    reload_btn.setStatusTip("Reload page")
    reload_btn.triggered.connect(
        lambda: self.tabs.currentWidget().reload())
    return reload_btn


def initHomeButton(self: QMainWindow):
    home_btn = QAction("Home", self)
    home_btn.setStatusTip("Go home")
    home_btn.triggered.connect(self.navigate_home)
    return home_btn


def initStopButton(self: QMainWindow):
    stop_btn = QAction("Stop", self)
    stop_btn.setStatusTip("Stop")
    stop_btn.triggered.connect(self.showHistory)
    return stop_btn


def initStarButton(self: QMainWindow):
    star_btn = QToolButton()
    star_btn.setIcon(QIcon("assets/images/star.png"))
    star_btn.clicked.connect(lambda: self.save_bookmark())
    return star_btn
