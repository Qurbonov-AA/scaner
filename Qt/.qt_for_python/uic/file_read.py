# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Desktop\bot\Qt\file_read.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(750, 545)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\User\\Desktop\\bot\\Qt\\icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 30, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 90, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 150, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 210, 341, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(600, 20, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 100, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 160, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(680, 220, 25, 19))
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.mybutton_clicked)
        self.pushButton_2.clicked.connect(Dialog.mybutton2_clicked)
        self.pushButton_3.clicked.connect(Dialog.mybutton3_clicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Reader"))
        self.pushButton.setText(_translate("Dialog", "First File"))
        self.pushButton_2.setText(_translate("Dialog", "Second File"))
        self.pushButton_3.setText(_translate("Dialog", "Thirty File"))
        self.pushButton_4.setText(_translate("Dialog", "Read Files"))
        self.pushButton_5.setText(_translate("Dialog", "Send File"))
        self.toolButton.setText(_translate("Dialog", "..."))
import images_rc
