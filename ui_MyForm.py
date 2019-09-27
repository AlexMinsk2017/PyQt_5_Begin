# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Project\PyQt_5_Begin\ui_MyForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewForm(object):
    def setupUi(self, NewForm):
        NewForm.setObjectName("NewForm")
        NewForm.resize(450, 150)
        self.centralwidget = QtWidgets.QWidget(NewForm)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btnQuit = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuit.setObjectName("btnQuit")
        self.verticalLayout.addWidget(self.btnQuit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        NewForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewForm)
        QtCore.QMetaObject.connectSlotsByName(NewForm)

    def retranslateUi(self, NewForm):
        _translate = QtCore.QCoreApplication.translate
        NewForm.setWindowTitle(_translate("NewForm", "Форма дизайнера"))
        self.label.setText(_translate("NewForm", "TextLabel"))
        self.btnQuit.setText(_translate("NewForm", "&Close window"))
