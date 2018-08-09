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
        
        # zoom to Milan when button is clicked
        self.btnGoTo.clicked.connect(self.on_btnGoTo_clicked)
    
    # https://stackoverflow.com/a/41780519/1979665
    # https://gist.github.com/epifanio/a1152047086def509906fa71a9eb11ad
    # https://stackoverflow.com/a/40553894/1979665
    @pyqtSlot()
    def on_btnGoTo_clicked(self):
        """
        Slot documentation goes here.
        """
        # Milan in EPSG 4326
        lng = 9.19034
        lat = 45.46416
        self.webView.page().runJavaScript('map.getView().animate({{center:[{lng}, {lat}], duration: 2000, zoom: 12}});'.format(lng = lng,  lat = lat),
                                                            self.js_callback)
        
    def js_callback(self,  result):
        print(result)
    
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
            
