__author__ = 'rais'
# -*- coding:utf-8 -*-
debug = 0
import nuke
import os

from functools import partial
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
#import PyQt4.QtCore as QtCore
#import PyQt4.QtGui as QtGui
from nukescripts import panels
import cPickle as pick
import json


class frameSnippetsPanel(QtGui.QWidget):
	""""""

	def __init__(self,  parent=None):
		"""Constructor for frameSnippetsPanel"""
		super(frameSnippetsPanel, self).__init__(parent)

		self.frameButtons ={}
		self.data = {}
		self.js_data = {}
		self.buttonName = None
		self.DBpath = None






		#====--------------------  按钮  --------------------====
		self.path = QtGui.QLabel('')
		self.delmodel = QtGui.QCheckBox('删除模式')
		self.addButton = self.createButton("记录当前帧", self.addSnip)


		#
		self.buttonsLayout = QtGui.QVBoxLayout()
		self.buttonsLayout.addWidget(self.path)
		self.buttonsLayout.addWidget(self.delmodel)
		self.buttonsLayout.addWidget(self.addButton)


		self.dynTab = QtGui.QTabWidget()



		self.mainLayout = QtGui.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonsLayout)
		self.mainLayout.addWidget(self.dynTab)


		self.setLayout(self.mainLayout)
		#====--------------------


		self.initDB()

		nuke.callbacks.addOnDestroy(self.onDestroyCallback, nodeClass='Viewer')
		nuke.callbacks.addOnScriptLoad(self.setDBpath, nodeClass='Root')



	def proDataSave(self):
		pathfile = self.DBpath
		jn_data = json.dumps(self.js_data)

		f = open(pathfile,'w')
		f.write(jn_data)
		f.close()

	def proDataLoad(self,pathfile):
		f = open(pathfile,'r')
		self.js_data = json.loads(f.read())
		f.close()



#	def proDataSave(self,data):
#		assert self.DBpath !=None
#		print os.getcwd()
#		f = open(self.DBpath,'w')
#		pick_data = pick.dump(data,f)
#		f.close()
#
#
#	def proDataLoad(self):
#		assert self.DBpath !=None
#		f = open(self.DBpath,'r')
#		pick_data = pick.load(f)
#		f.close()
#		print pick_data
#		return pick_data


	def initDB(self):
		self.setDBpath()
		assert self.DBpath !=None
		self.path.setText(self.DBpath)
		if os.path.exists(self.DBpath):
			self.proDataLoad(self.DBpath)
			self.loadButtonFromDB()

	def loadButtonFromDB(self):
		for vName in self.js_data.keys():
			for frame,bName in self.js_data[vName]['frame'].iteritems():
				self.addSnip(vName,frame,bName)




	def setDBpath(self):
		fn = self.getFileName()
		if fn == '':
			fn = os.getenv('NUKE_TEMP_DIR')+'/'

		self.DBpath = fn +'_frameSnip.db'

	def getFileName(self):
		return nuke.toNode('root').knob('name').value()

	def onDestroyCallback(self):
		vName = nuke.thisNode().name()
		if vName in self.data.keys():
			bs = self.data[vName]['frame'].values()
			for b in bs:    del self.frameButtons[b]
			self.data[vName]['obj'].deleteLater()
			del self.data[vName]

	def createButton(self, text, member):
		'''创建按钮包装'''
		button = QtGui.QPushButton(text)

		button.clicked.connect(member)
		return button

	def remove(self):
		nuke.callbacks.removeOnDestroy(self.onCreateCallback, args=(), kwargs={}, nodeClass='Viewer')
		print 'remove'

	def getName(self):
		u'''
		弹出命名窗口
		'''
		inputName = QtGui.QDialog(self)
		#

		inNameL = QtGui.QLabel('命名')
		inNameLE = QtGui.QLineEdit('')
		inNameDBB = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Save|QtGui.QDialogButtonBox.Cancel)


		inputNameMainLay = QtGui.QVBoxLayout()
		inputNameMainLay.addWidget(inNameL)
		inputNameMainLay.addWidget(inNameLE)
		inputNameMainLay.addWidget(inNameDBB)

		inputName.setLayout(inputNameMainLay)



		callback = partial(self.nameDialogAccept,inNameLE)
		inNameDBB.accepted.connect(callback)
		inNameDBB.accepted.connect(inputName.accept)
		inNameDBB.rejected.connect(self.nameDialogReject)
		inNameDBB.rejected.connect(inputName.reject)


		inputName.show()
		inputName.exec_()
		return  self.buttonName

	def nameDialogAccept(self,LE):
		self.buttonName = LE.text()

	def nameDialogReject(self):
		self.buttonName = None


	def frameDo(self):
		b = self.sender()
		if b is None or not isinstance(b, QtGui.QPushButton):return

		if not self.delmodel.isChecked():
			vName,frame = self.frameButtons[b]
			nuke.toNode(vName).knob('frame').setValue(int(frame))
		else:
			print 'del'
			vName,frame = self.frameButtons.pop(b)
			self.data[vName]['frame'].pop(frame).deleteLater()
			del self.js_data[vName]['frame'][frame]
			self.chkTab(vName)
			self.proDataSave()


	def chkTab(self,vName):
		#print 'keys',self.data[vName]['frame'].keys()
		if len(self.data[vName]['frame'].keys()) == 0:
			self.data[vName]['obj'].deleteLater()
			del self.data[vName]
			del self.js_data[vName]



	def addSnip(self,vName = None,frame=None,bName = None ):
		addFromDB = 1
		if vName is None:
			addFromDB = 0
			vName = nuke.activeViewer().node().name()
		if frame is None:
			frame = nuke.activeViewer().node().knob('frame').value()
			frame = str(int(frame))

		if debug:print vName,frame
		if vName not in self.data.keys():
			frameTabObj = QtGui.QWidget()
			frameTabObjLay = QtGui.QHBoxLayout()
			frameTabObj.setLayout(frameTabObjLay)
			self.dynTab.addTab(frameTabObj,vName)
			self.data[vName] = {}
			self.js_data[vName] = {}
			self.data[vName]['frame'] = {}
			self.js_data[vName]['frame'] = {}
			self.data[vName]['lay'] = frameTabObjLay
			self.data[vName]['obj'] = frameTabObj
			if debug:print self.js_data,self.data





		if frame not in self.data[vName]['frame'].keys():
			if bName is None:bName = self.getName()
			if bName != None:
				b = self.createButton("%s : %s" % (frame,bName),self.frameDo)
				b.setMaximumWidth(300)
				self.data[vName]['frame'][frame] = b
				self.js_data[vName]['frame'][frame] = bName
				self.data[vName]['lay'].addWidget(b)
				self.frameButtons[b] = (vName,frame)
				if debug:print self.js_data,self.data

		if not addFromDB:self.proDataSave()



	panels.registerWidgetAsPanel('frameSnippetsPanel', '时间帧收藏', 'uk.co.thefoundry.frameSnippetsPanel')

