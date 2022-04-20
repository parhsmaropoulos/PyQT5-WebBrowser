from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import qtawesome as qta
from bookmarks import *


def initNextButton(self: QMainWindow):
    next_btn = QAction("Forward", self)
    next_btn.setStatusTip("Forward to next page")
    next_btn.setIcon(QIcon(qta.icon('ph.arrow-circle-right')))
    next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
    return next_btn


def initBackButton(self: QMainWindow):
    back_btn = QAction("Back", self)
    back_btn.setStatusTip("Back to previous page")
    back_btn.setIcon(QIcon(qta.icon('ph.arrow-circle-left')))
    back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

    return back_btn


def initReloadButton(self: QMainWindow):
    reload_btn = QAction("Reload", self)
    reload_btn.setStatusTip("Reload page")
    reload_btn.setIcon(QIcon(qta.icon('ph.arrows-clockwise')))
    reload_btn.triggered.connect(
        lambda: self.tabs.currentWidget().reload())
    return reload_btn


def initHomeButton(self: QMainWindow):
    home_btn = QAction("Home", self)
    home_btn.setStatusTip("Go home")
    home_btn.setIcon(QIcon(qta.icon('ph.house')))
    home_btn.triggered.connect(self.navigate_home)
    return home_btn


def initStopButton(self: QMainWindow):
    stop_btn = QAction("Stop", self)
    stop_btn.setStatusTip("Stop")
    stop_btn.triggered.connect(self.show_history)
    return stop_btn


def initStarButton(self: QMainWindow):
    star_btn = QToolButton()
    star_btn.setIcon(QIcon(qta.icon('ph.star')))
    star_btn.clicked.connect(lambda: self.save_bookmark())
    return star_btn


def initSettingsButton(self: QMainWindow):
    settings_btn = QToolButton()
    settings_btn.setIcon(QIcon(qta.icon('ph.list')))
    settings_btn.clicked.connect(self.show_settings)
    return settings_btn
