# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import os.path
from PyQt5.QtCore import pyqtSlot,  QUrl
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWebChannel import QWebChannel

from .ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        dirname = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(dirname)
        html = 'map.html'
        url = QUrl.fromLocalFile(os.path.join(root_dir,  html))
        self.webView.load(url)
        
        # https://stackoverflow.com/questions/41877799/get-dynamic-content-using-pyqt
        self.webchannel = QWebChannel(self)
        self.webView.page().setWebChannel(self.webchannel)
        self.webchannel.registerObject('MyChannel', self)
    
    @pyqtSlot()
    def on_btnMilan_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(bool)
    def on_webView_loadFinished(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        pass
        
    # https://stackoverflow.com/questions/41877799/get-dynamic-content-using-pyqt
    # https://stackoverflow.com/questions/28565254/how-to-use-qt-webengine-and-qwebchannel
    @pyqtSlot(str)
    def set_lbl_coord(self,  map_center = None):
        """
        Slot documentation goes here.
        """
        if map_center:
            self.lblCoord.setText(map_center)
            
