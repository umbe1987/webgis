# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/umberto/Documents/apps/projects/webgis/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 531)
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
        self.btnGoTo = QtWidgets.QPushButton(self.centralWidget)
        self.btnGoTo.setObjectName("btnGoTo")
        self.gridLayout.addWidget(self.btnGoTo, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblCoord.setText(_translate("MainWindow", "lblCoord"))
        self.btnGoTo.setText(_translate("MainWindow", "Go to Location"))

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

