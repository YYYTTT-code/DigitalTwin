# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DigitalTwinShowUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(838, 550)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(450, 480, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.showButton = QtWidgets.QPushButton(Dialog)
        self.showButton.setGeometry(QtCore.QRect(310, 170, 221, 41))
        self.showButton.setObjectName("showButton")
        self.miniumButton = QtWidgets.QPushButton(Dialog)
        self.miniumButton.setGeometry(QtCore.QRect(590, 30, 75, 23))
        self.miniumButton.setText("")
        self.miniumButton.setObjectName("miniumButton")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(680, 30, 75, 23))
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.miniumButton.clicked.connect(Dialog.showMinimized)
        self.closeButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.showButton.setText(_translate("Dialog", "打开远程屏幕"))
