#!/usr/bin/env python
# -*- coding: utf-8 -*-
# converted from C++ by blindvic
"""
PyQt version of Window Flags Example
http://doc.trolltech.com/4.6/widgets-windowflags.html
"""

import sys, os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class PreviewWindow ( QWidget ) :
	def __init__ ( self, parent = None ) :
		QWidget.__init__ ( self, parent )
		self.textEdit = QTextEdit ()
		self.textEdit.setReadOnly ( True )
		self.textEdit.setLineWrapMode ( QTextEdit.NoWrap )

		self.closeButton = QPushButton ( "&Close" )
		self.closeButton.clicked.connect ( self.close )

		layout = QVBoxLayout ()
		layout.addWidget ( self.textEdit )
		layout.addWidget ( self.closeButton )
		self.setLayout ( layout )

		self.setWindowTitle ( "Preview" )

	def setWindowFlags ( self, flags ) :

		QWidget.setWindowFlags ( self, flags )

		text = ""

		type = flags & Qt.WindowType_Mask
		if type == Qt.Window :
			text = "Qt.Window"
		elif type == Qt.Dialog :
			text = "Qt.Dialog"
		elif type == Qt.Sheet :
			text = "Qt.Sheet"
		elif type == Qt.Drawer :
			text = "Qt.Drawer"
		elif type == Qt.Popup :
			text = "Qt.Popup"
		elif type == Qt.Tool :
			text = "Qt.Tool"
		elif type == Qt.ToolTip :
			text = "Qt.ToolTip"
		elif type == Qt.SplashScreen :
			text = "Qt.SplashScreen"

		if flags & Qt.MSWindowsFixedSizeDialogHint :
			text += "\n| Qt.MSWindowsFixedSizeDialogHint"
		if flags & Qt.X11BypassWindowManagerHint :
			text += "\n| Qt.X11BypassWindowManagerHint"
		if flags & Qt.FramelessWindowHint :
			text += "\n| Qt.FramelessWindowHint"
		if flags & Qt.WindowTitleHint :
			text += "\n| Qt.WindowTitleHint"
		if flags & Qt.WindowSystemMenuHint :
			text += "\n| Qt.WindowSystemMenuHint"
		if flags & Qt.WindowMinimizeButtonHint :
			text += "\n| Qt.WindowMinimizeButtonHint"
		if flags & Qt.WindowMaximizeButtonHint :
			text += "\n| Qt.WindowMaximizeButtonHint"
		if flags & Qt.WindowCloseButtonHint :
			text += "\n| Qt.WindowCloseButtonHint"
		if flags & Qt.WindowContextHelpButtonHint :
			text += "\n| Qt.WindowContextHelpButtonHint"
		if flags & Qt.WindowShadeButtonHint :
			text += "\n| Qt.WindowShadeButtonHint"
		if flags & Qt.WindowStaysOnTopHint :
			text += "\n| Qt.WindowStaysOnTopHint"
		if flags & Qt.CustomizeWindowHint :
			text += "\n| Qt.CustomizeWindowHint"

		self.textEdit.setPlainText ( text )


class ControllerWindow ( QWidget ) :

	def __init__ ( self, parent = None ) :
		QWidget.__init__ ( self, parent )

		self.previewWindow = PreviewWindow ( self )

		self.createTypeGroupBox ()
		self.createHintsGroupBox ()

		self.quitButton = QPushButton ( "&Quit" )
		self.quitButton.clicked.connect ( self.close )

		bottomLayout = QHBoxLayout ()
		bottomLayout.addStretch ()
		bottomLayout.addWidget ( self.quitButton )

		mainLayout = QVBoxLayout ()
		mainLayout.addWidget ( self.typeGroupBox )
		mainLayout.addWidget ( self.hintsGroupBox )
		mainLayout.addLayout ( bottomLayout )
		self.setLayout ( mainLayout )

		self.setWindowTitle ( "Window Flags" )
		self.updatePreview ()

	def updatePreview ( self ) :
		flags = 0

		if self.windowRadioButton.isChecked () :
			flags = Qt.Window
		elif self.dialogRadioButton.isChecked () :
			flags = Qt.Dialog
		elif self.sheetRadioButton.isChecked () :
			flags = Qt.Sheet
		elif self.drawerRadioButton.isChecked () :
			flags = Qt.Drawer
		elif self.popupRadioButton.isChecked () :
			flags = Qt.Popup
		elif self.toolRadioButton.isChecked () :
			flags = Qt.Tool
		elif self.toolTipRadioButton.isChecked () :
			flags = Qt.ToolTip
		elif self.splashScreenRadioButton.isChecked () :
			flags = Qt.SplashScreen

		if self.msWindowsFixedSizeDialogCheckBox.isChecked () :
			flags |= Qt.MSWindowsFixedSizeDialogHint
		if self.x11BypassWindowManagerCheckBox.isChecked () :
			flags |= Qt.X11BypassWindowManagerHint
		if self.framelessWindowCheckBox.isChecked () :
			flags |= Qt.FramelessWindowHint
		if self.windowTitleCheckBox.isChecked () :
			flags |= Qt.WindowTitleHint
		if self.windowSystemMenuCheckBox.isChecked () :
			flags |= Qt.WindowSystemMenuHint
		if self.windowMinimizeButtonCheckBox.isChecked () :
			flags |= Qt.WindowMinimizeButtonHint
		if self.windowMaximizeButtonCheckBox.isChecked () :
			flags |= Qt.WindowMaximizeButtonHint
		if self.windowCloseButtonCheckBox.isChecked () :
			flags |= Qt.WindowCloseButtonHint
		if self.windowContextHelpButtonCheckBox.isChecked () :
			flags |= Qt.WindowContextHelpButtonHint
		if self.windowShadeButtonCheckBox.isChecked () :
			flags |= Qt.WindowShadeButtonHint
		if self.windowStaysOnTopCheckBox.isChecked () :
			flags |= Qt.WindowStaysOnTopHint
		if self.windowStaysOnBottomCheckBox.isChecked () :
			flags |= Qt.WindowStaysOnBottomHint
		if self.customizeWindowHintCheckBox.isChecked () :
			flags |= Qt.CustomizeWindowHint

		self.previewWindow.setWindowFlags ( flags )

		pos = self.previewWindow.pos ()
		if pos.x () < 0 :
			pos.setX ( 0 )
		if pos.y () < 0 :
			pos.setY ( 0 )
		self.previewWindow.move ( pos )
		self.previewWindow.show ()


	def createTypeGroupBox ( self ) :
		self.typeGroupBox = QGroupBox ( "Type" )

		self.windowRadioButton = self.createRadioButton ( "Window" )
		self.dialogRadioButton = self.createRadioButton ( "Dialog" )
		self.sheetRadioButton = self.createRadioButton ( "Sheet" )
		self.drawerRadioButton = self.createRadioButton ( "Drawer" )
		self.popupRadioButton = self.createRadioButton ( "Popup" )
		self.toolRadioButton = self.createRadioButton ( "Tool" )
		self.toolTipRadioButton = self.createRadioButton ( "Tooltip" )
		self.splashScreenRadioButton = self.createRadioButton ( "Splash screen" )
		self.windowRadioButton.setChecked ( True )

		layout = QGridLayout ()
		layout.addWidget ( self.windowRadioButton, 0, 0 )
		layout.addWidget ( self.dialogRadioButton, 1, 0 )
		layout.addWidget ( self.sheetRadioButton, 2, 0 )
		layout.addWidget ( self.drawerRadioButton, 3, 0 )
		layout.addWidget ( self.popupRadioButton, 0, 1 )
		layout.addWidget ( self.toolRadioButton, 1, 1 )
		layout.addWidget ( self.toolTipRadioButton, 2, 1 )
		layout.addWidget ( self.splashScreenRadioButton, 3, 1 )
		self.typeGroupBox.setLayout ( layout )

	def createRadioButton ( self, text ) :
		button = QRadioButton ( text )
		button.clicked.connect ( self.updatePreview )
		return button

	def createHintsGroupBox ( self ) :
		self.hintsGroupBox = QGroupBox ( "Hints" )

		self.msWindowsFixedSizeDialogCheckBox = self.createCheckBox ( "MS Windows fixed size dialog" )
		self.x11BypassWindowManagerCheckBox = self.createCheckBox ( "X11 bypass window manager" )
		self.framelessWindowCheckBox = self.createCheckBox ( "Frameless window")
		self.windowTitleCheckBox = self.createCheckBox ( "Window title" )
		self.windowSystemMenuCheckBox = self.createCheckBox ( "Window system menu" )
		self.windowMinimizeButtonCheckBox = self.createCheckBox ( "Window minimize button" )
		self.windowMaximizeButtonCheckBox = self.createCheckBox ( "Window maximize button" )
		self.windowCloseButtonCheckBox = self.createCheckBox ( "Window close button" )
		self.windowContextHelpButtonCheckBox = self.createCheckBox ( "Window context help button" )
		self.windowShadeButtonCheckBox = self.createCheckBox ( "Window shade button" )
		self.windowStaysOnTopCheckBox = self.createCheckBox ( "Window stays on top" )
		self.windowStaysOnBottomCheckBox = self.createCheckBox ( "Window stays on bottom" )
		self.customizeWindowHintCheckBox = self.createCheckBox ( "Customize window" )

		layout = QGridLayout ()
		layout.addWidget ( self.msWindowsFixedSizeDialogCheckBox, 0, 0 )
		layout.addWidget ( self.x11BypassWindowManagerCheckBox, 1, 0 )
		layout.addWidget ( self.framelessWindowCheckBox, 2, 0 )
		layout.addWidget ( self.windowTitleCheckBox, 3, 0 )
		layout.addWidget ( self.windowSystemMenuCheckBox, 4, 0 )
		layout.addWidget ( self.windowMinimizeButtonCheckBox, 0, 1 )
		layout.addWidget ( self.windowMaximizeButtonCheckBox, 1, 1 )
		layout.addWidget ( self.windowCloseButtonCheckBox, 2, 1 )
		layout.addWidget ( self.windowContextHelpButtonCheckBox, 3, 1 )
		layout.addWidget ( self.windowShadeButtonCheckBox, 4, 1 )
		layout.addWidget ( self.windowStaysOnTopCheckBox, 5, 1 )
		layout.addWidget ( self.windowStaysOnBottomCheckBox, 6, 1 )
		layout.addWidget ( self.customizeWindowHintCheckBox, 5, 0 )
		self.hintsGroupBox.setLayout ( layout )


	def createCheckBox ( self, text ) :
		checkBox = QCheckBox ( text )
		checkBox.clicked.connect ( self.updatePreview )
		return checkBox


def main () :
	#app = QApplication ( sys.argv )
	global controller
	controller= ControllerWindow ()
	controller.show ()
	#sys.exit ( app.exec_ () )

if __name__ == '__main__' : main()