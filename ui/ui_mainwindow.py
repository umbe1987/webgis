# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\DATI\git\webgis\ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 824)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblCoord = QtWidgets.QLabel(self.centralWidget)
        self.lblCoord.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblCoord.setFont(font)
        self.lblCoord.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCoord.setObjectName("lblCoord")
        self.gridLayout.addWidget(self.lblCoord, 0, 0, 1, 1)
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralWidget)
        self.webView.setObjectName("webView")
        self.gridLayout.addWidget(self.webView, 1, 0, 1, 1)
        self.btnMilan = QtWidgets.QPushButton(self.centralWidget)
        self.btnMilan.setObjectName("btnMilan")
        self.gridLayout.addWidget(self.btnMilan, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblCoord.setText(_translate("MainWindow", "lblCoord"))
        self.btnMilan.setText(_translate("MainWindow", "Go to Milan"))

from PyQt5 import QtWebEngineWidgets
