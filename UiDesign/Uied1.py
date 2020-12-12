# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Uied1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 446)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(20, 10, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 120, 530, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.portReceive = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.portReceive.setFont(font)
        self.portReceive.setObjectName("portReceive")
        self.gridLayout.addWidget(self.portReceive, 0, 0, 1, 1)
        self.weldingParaPredict = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.weldingParaPredict.setFont(font)
        self.weldingParaPredict.setObjectName("weldingParaPredict")
        self.gridLayout.addWidget(self.weldingParaPredict, 1, 0, 1, 1)
        self.qualityPrediction = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.qualityPrediction.setFont(font)
        self.qualityPrediction.setObjectName("qualityPrediction")
        self.gridLayout.addWidget(self.qualityPrediction, 1, 1, 1, 1)
        self.machineLearnTrain = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.machineLearnTrain.setFont(font)
        self.machineLearnTrain.setObjectName("machineLearnTrain")
        self.gridLayout.addWidget(self.machineLearnTrain, 0, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(490, 20, 158, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.miniumButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.miniumButton.setObjectName("miniumButton")
        self.horizontalLayout.addWidget(self.miniumButton)
        self.closeButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.closeButton.clicked.connect(MainWindow.close)
        self.miniumButton.clicked.connect(MainWindow.lower)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #  窗口美化
        MainWindow.setWindowOpacity(0.9)  # 设置窗口透明度
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.closeButton.setFixedSize(15,15)
        self.miniumButton.setFixedSize(15,15)
        self.closeButton.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.miniumButton.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "船厂中小组立件数字孪生系统"))
        self.title.setText(_translate("MainWindow", "船厂中小组立件数组孪生系统"))
        self.portReceive.setText(_translate("MainWindow", "串口接收"))
        self.weldingParaPredict.setText(_translate("MainWindow", "焊接参数预测"))
        self.qualityPrediction.setText(_translate("MainWindow", "焊后性能预测"))
        self.machineLearnTrain.setText(_translate("MainWindow", "机器模型训练"))
        # self.miniumButton.setText(_translate("MainWindow", "最小化"))
        # self.closeButton.setText(_translate("MainWindow", "关闭"))

