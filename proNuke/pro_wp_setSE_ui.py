# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pro_wp_setSE.ui'
#
# Created: Mon Feb  4 10:59:02 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(279, 101)
        Dialog.setModal(False)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sQSB = QtGui.QSpinBox(Dialog)
        self.sQSB.setWrapping(False)
        self.sQSB.setAccelerated(False)
        self.sQSB.setMinimum(-999)
        self.sQSB.setMaximum(999999)
        self.sQSB.setObjectName("sQSB")
        self.horizontalLayout.addWidget(self.sQSB)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.eQSB = QtGui.QSpinBox(Dialog)
        self.eQSB.setMinimum(-999)
        self.eQSB.setMaximum(999999)
        self.eQSB.setObjectName("eQSB")
        self.horizontalLayout.addWidget(self.eQSB)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.setQPB = QtGui.QPushButton(Dialog)
        self.setQPB.setObjectName("setQPB")
        self.verticalLayout.addWidget(self.setQPB)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.setQPB, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "批量设置3屏节点的 开始结束帧", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "end", None, QtGui.QApplication.UnicodeUTF8))
        self.setQPB.setText(QtGui.QApplication.translate("Dialog", "set", None, QtGui.QApplication.UnicodeUTF8))

