# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serialUi_diag.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(867, 517)
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(710, 40, 31, 23))
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.stopButton = QtWidgets.QPushButton(Dialog)
        self.stopButton.setGeometry(QtCore.QRect(500, 390, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.miniumButton = QtWidgets.QPushButton(Dialog)
        self.miniumButton.setGeometry(QtCore.QRect(670, 40, 31, 23))
        self.miniumButton.setText("")
        self.miniumButton.setObjectName("miniumButton")
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(180, 390, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 200, 181, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Vlabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.Vlabel.setFont(font)
        self.Vlabel.setObjectName("Vlabel")
        self.horizontalLayout_2.addWidget(self.Vlabel)
        self.VlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.VlineEdit.setObjectName("VlineEdit")
        self.horizontalLayout_2.addWidget(self.VlineEdit)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(130, 120, 181, 27))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Alabel = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.Alabel.setFont(font)
        self.Alabel.setObjectName("Alabel")
        self.horizontalLayout.addWidget(self.Alabel)
        self.AlineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.AlineEdit.setObjectName("AlineEdit")
        self.horizontalLayout.addWidget(self.AlineEdit)
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(70, 290, 244, 27))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Llabel = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.Llabel.setFont(font)
        self.Llabel.setObjectName("Llabel")
        self.horizontalLayout_3.addWidget(self.Llabel)
        self.LlineEdit = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.LlineEdit.setObjectName("LlineEdit")
        self.horizontalLayout_3.addWidget(self.LlineEdit)

        self.retranslateUi(Dialog)
        self.miniumButton.clicked.connect(Dialog.lower)
        self.closeButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.stopButton.setText(_translate("Dialog", "结束"))
        self.startButton.setText(_translate("Dialog", "开始"))
        self.Vlabel.setText(_translate("Dialog", "电压："))
        self.Alabel.setText(_translate("Dialog", "电流："))
        self.Llabel.setText(_translate("Dialog", "保护气流量："))
