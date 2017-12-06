# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setGeometry(QtCore.QRect(230, 50, 341, 501))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.lblCoord = QtWidgets.QLabel(self.splitter)
        self.lblCoord.setObjectName("lblCoord")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.splitter)
        self.webView.setObjectName("webView")
        self.btnMilan = QtWidgets.QPushButton(self.splitter)
        self.btnMilan.setObjectName("btnMilan")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblCoord.setText(_translate("MainWindow", "lblCoord"))
        self.btnMilan.setText(_translate("MainWindow", "Go to Milan"))

from PyQt5 import QtWebEngineWidgets
