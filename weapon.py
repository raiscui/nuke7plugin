#!/usr/bin/env python

# coding=utf-8
# Author:  rais --<cgengine>
# Purpose: 武器,---- 普罗米修斯系统 NUKE类
# Created: 2012/9/20
import sys, os.path
import nuke
from PyQt4 import QtCore, QtGui, uic

class setFrameUI(QtGui.QDialog):
	def __init__(self, parent=None):
		super(setFrameUI, self).__init__(parent)
		self.aa =  QtGui.QPushButton('remove')
		mainLayout = QtGui.QGridLayout()
		mainLayout.addWidget(self.aa)
		self.setLayout(mainLayout)

class setFrame(object):
	def __init__(self, parent =None):
		super(setFrame, self).__init__()
		self.parent = parent
		self.ui = setFrameUI(self.parent)
		nuke.callbacks.addOnCreate(self.onCreateCallback, args=(), kwargs={}, nodeClass='Write')
		
		self.ui.aa.clicked.connect(self.remove)
		self.ui.accepted.connect(self.remove)
		self.ui.finished.connect(self.remove)
		self.ui.rejected.connect(self.remove)
		
		


	def showUI(self):
		self.ui.show()
		
	def onCreateCallback(self, *arg):
		n = nuke.thisNode()
		for a in arg:print a
		print 'wwwwwwww'
		print 'name', n.name()
		if n.Class() == "Write":
			n.setName(n.name())
			
	def remove(self):
		nuke.callbacks.removeOnCreate(self.onCreateCallback, args=(), kwargs={}, nodeClass='Write')
		print 'remove'

			

def initRenderDialog():


	global dialog
	dialog = setFrame()
	dialog.showUI()
	
initRenderDialog()