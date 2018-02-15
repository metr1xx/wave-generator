# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GitHub/wave-generator/wavegenerator.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(299, 202)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 281, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopContainer = QtWidgets.QHBoxLayout()
        self.TopContainer.setObjectName("TopContainer")
        self.WaveContainer = QtWidgets.QVBoxLayout()
        self.WaveContainer.setObjectName("WaveContainer")
        self.SineWaveRadio = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.SineWaveRadio.setObjectName("SineWaveRadio")
        self.WaveContainer.addWidget(self.SineWaveRadio)
        self.SawWaveRadio = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.SawWaveRadio.setObjectName("SawWaveRadio")
        self.WaveContainer.addWidget(self.SawWaveRadio)
        self.TriangleWaveRadio = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.TriangleWaveRadio.setObjectName("TriangleWaveRadio")
        self.WaveContainer.addWidget(self.TriangleWaveRadio)
        self.SquareWaveRadio = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.SquareWaveRadio.setObjectName("SquareWaveRadio")
        self.WaveContainer.addWidget(self.SquareWaveRadio)
        self.TopContainer.addLayout(self.WaveContainer)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.TopContainer.addItem(spacerItem)
        self.FileTimeContainer = QtWidgets.QVBoxLayout()
        self.FileTimeContainer.setObjectName("FileTimeContainer")
        self.FileNameBox = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.FileNameBox.setObjectName("FileNameBox")
        self.FileTimeContainer.addWidget(self.FileNameBox)
        self.PlaytimeSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.PlaytimeSpinBox.setObjectName("PlaytimeSpinBox")
        self.FileTimeContainer.addWidget(self.PlaytimeSpinBox)
        self.TopContainer.addLayout(self.FileTimeContainer)
        self.verticalLayout.addLayout(self.TopContainer)
        self.ButtonContainer = QtWidgets.QHBoxLayout()
        self.ButtonContainer.setObjectName("ButtonContainer")
        self.CreateWaveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CreateWaveButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CreateWaveButton.setObjectName("CreateWaveButton")
        self.ButtonContainer.addWidget(self.CreateWaveButton)
        self.ExitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ExitButton.setEnabled(True)
        self.ExitButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ExitButton.setObjectName("ExitButton")
        self.ButtonContainer.addWidget(self.ExitButton)
        self.verticalLayout.addLayout(self.ButtonContainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SineWaveRadio.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create a sine wave.</p></body></html>"))
        self.SineWaveRadio.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Create a sine wave.</p></body></html>"))
        self.SineWaveRadio.setText(_translate("MainWindow", "Sine Wave"))
        self.SawWaveRadio.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create a saw wave.</p></body></html>"))
        self.SawWaveRadio.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Create a saw wave.</p></body></html>"))
        self.SawWaveRadio.setText(_translate("MainWindow", "Saw Wave"))
        self.TriangleWaveRadio.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create a triangle wave.</p></body></html>"))
        self.TriangleWaveRadio.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Create a triangle wave.</p></body></html>"))
        self.TriangleWaveRadio.setText(_translate("MainWindow", "Triangle Wave"))
        self.SquareWaveRadio.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create a square wave.</p></body></html>"))
        self.SquareWaveRadio.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Create a square wave.</p></body></html>"))
        self.SquareWaveRadio.setText(_translate("MainWindow", "Square Wave"))
        self.FileNameBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Input the name of the file you want to create. Files that exist will be overwritten.</p></body></html>"))
        self.FileNameBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Input the name of the file you want to create. Files that exist will be overwritten.</p></body></html>"))
        self.FileNameBox.setText(_translate("MainWindow", "File Name"))
        self.PlaytimeSpinBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Playtime of the created wave in Seconds.</p></body></html>"))
        self.PlaytimeSpinBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Playtime of the created wave in Seconds.</p></body></html>"))
        self.CreateWaveButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create the waveform and store it in a file.</p></body></html>"))
        self.CreateWaveButton.setText(_translate("MainWindow", "Create Wave!"))
        self.ExitButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Exit this Program.</p></body></html>"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))
