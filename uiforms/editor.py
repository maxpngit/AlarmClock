# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


# дизайн формы для редактирования будильников
class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(390, 308)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Editor.sizePolicy().hasHeightForWidth())
        Editor.setSizePolicy(sizePolicy)
        Editor.setMinimumSize(QtCore.QSize(390, 308))
        Editor.setMaximumSize(QtCore.QSize(390, 308))
        Editor.setBaseSize(QtCore.QSize(390, 308))
        self.NameLine = QtWidgets.QLineEdit(Editor)
        self.NameLine.setGeometry(QtCore.QRect(10, 110, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.NameLine.setFont(font)
        self.NameLine.setObjectName("NameLine")
        self.MusicList = QtWidgets.QListWidget(Editor)
        self.MusicList.setGeometry(QtCore.QRect(10, 150, 371, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.MusicList.setFont(font)
        self.MusicList.setObjectName("MusicList")
        self.Save = QtWidgets.QPushButton(Editor)
        self.Save.setGeometry(QtCore.QRect(260, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Save.setFont(font)
        self.Save.setObjectName("Save")
        self.label = QtWidgets.QLabel(Editor)
        self.label.setGeometry(QtCore.QRect(10, 20, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(_translate("Editor", "Редактирование"))
        self.NameLine.setPlaceholderText(_translate("Editor", "Введите новое название"))
        self.Save.setText(_translate("Editor", "Сохранить"))
        self.label.setText(_translate("Editor", "Время срабытывания:"))
