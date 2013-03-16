#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
# Author:  rais --<cgengine>
# Purpose: wp,---- Prometeus NUKE class
# Created: 2012/9/20
import sys, os.path
import nuke

#from PyQt4 import QtCore, QtGui, Pyuic
from PySide import QtCore,QtGui
from pro_wp_setSE_ui import Ui_Dialog


debug = 0


########################################################################
class proNF3pnode(object):
	u"""三屏节点设置工场"""

	#----------------------------------------------------------------------
	def __init__(self, objs = None):
		u"""Constructor"""
		self.objs =  None
		if debug:print objs, 'proNF3P init'
		if objs:self.setobjs(objs)

	def setobjs(self, objs):
		self.objs =  objs
	def getobjs (self):
		return self.objs

	def setStartEnd(self, ss,ee):
		sns =  self.getobjs()
		if debug:print sns, 'setStartEnd'
		for sn in sns:
			try:
				f = sn.node('Read39').knob('first')
				fv = ss
				f.setValue(int(fv))
				#f.setExpression(fv)

				s = sn.node('Read39').knob('last')
				sv = ee
				s.setValue(int(sv))
				#s.setExpression(sv)

				of = sn.node('Read39').knob('origfirst')
				ofv =ss
				of.setValue(int(ofv))

				os = sn.node('Read39').knob('origlast')
				osv =ee
				os.setValue(int(osv))

				self.resetStarEndEXP()


			except:
				pass
		for sn in sns:
			try:
				sn.node('Read39').knob('after').setValue(3)
				sn.node('Read39').knob('before').setValue(3)
			except:
				pass

	def resetStarEndEXP(self):
		sns =  self.getobjs()
		if debug:print sns, 'resetStarEndEXP'
		for sn in sns:
			try:

				#----------------------------------------------------------------------
				f = sn.node('Read1').knob('first')
				fv = 'parent.Read39.first'
				f.clearAnimated()
				f.setExpression(fv)

				s = sn.node('Read1').knob('last')
				sv = 'parent.Read39.last'
				s.clearAnimated()
				s.setExpression(sv)

				of = sn.node('Read1').knob('origfirst')
				ofv ='parent.Read39.origfirst'
				of.clearAnimated()
				of.setExpression(ofv)

				os = sn.node('Read1').knob('origlast')
				osv ='parent.Read39.origlast'
				os.clearAnimated()
				os.setExpression(osv)

				#----------------------------------------------------------------------
				f = sn.node('Read3').knob('first')
				fv = 'parent.Read39.first'
				f.clearAnimated()
				f.setExpression(fv)


				s = sn.node('Read3').knob('last')
				sv = 'parent.Read39.last'
				s.clearAnimated()
				s.setExpression(sv)

				of = sn.node('Read3').knob('origfirst')
				ofv ='parent.Read39.origfirst'
				of.clearAnimated()
				of.setExpression(ofv)

				os = sn.node('Read3').knob('origlast')
				osv ='parent.Read39.origlast'
				os.clearAnimated()
				os.setExpression(osv)
			except:
				pass


	def dumpPath(self):
		sns =  self.getobjs()
		if debug:print sns, 'dumpPath'
		for sn in sns:
			try:
				rp = sn.knob('rootp')
				rpv = rp.value()
				realpath = nuke.toNode(rpv).knob('label').value()
				rp.setValue(realpath)

				#----------------------------------------------------------------------
				f = sn.node('Read39').knob('file')
				fv =f.value()
				fv = fv.replace('[knob [knob parent.rootp].label]','[knob parent.rootp]')
				f.setValue(fv)
				#----------------------------------------------------------------------
				#----------------------------------------------------------------------
				f = sn.node('Read1').knob('file')
				fv =f.value()
				fv = fv.replace('[knob [knob parent.rootp].label]','[knob parent.rootp]')
				f.setValue(fv)
				#----------------------------------------------------------------------
				#----------------------------------------------------------------------
				f = sn.node('Read3').knob('file')
				fv =f.value()
				fv = fv.replace('[knob [knob parent.rootp].label]','[knob parent.rootp]')
				f.setValue(fv)
				#----------------------------------------------------------------------

			except Exception,e:
				print e


	def setCacheAlways(self):
		sns =  self.getobjs()
		if debug:print sns, 'setCacheAlways'
		for sn in sns:
			try:
				fv ='always'
				#----------------------------------------------------------------------
				f = sn.node('Read39').knob('cacheLocal')

				f.setValue(fv)
				#----------------------------------------------------------------------
				#----------------------------------------------------------------------
				f = sn.node('Read1').knob('cacheLocal')

				f.setValue(fv)
				#----------------------------------------------------------------------
				#----------------------------------------------------------------------
				f = sn.node('Read3').knob('cacheLocal')

				f.setValue(fv)
			#----------------------------------------------------------------------

			except Exception,e:
				print e

	def setCacheAuto(self):
		sns =  self.getobjs()
		if debug:print sns, 'setCacheAuto'
		for sn in sns:
			try:
				fv ='auto'
				#----------------------------------------------------------------------
				f = sn.node('Read39').knob('cacheLocal')

				f.setValue(fv)
				#----------------------------------------------------------------------
				#----------------------------------------------------------------------
				f = sn.node('Read1').knob('cacheLocal')

				f.setValue(fv)
				#----------------------------------------------------------------------
				#----------------------------------------------------------------------
				f = sn.node('Read3').knob('cacheLocal')

				f.setValue(fv)
			#----------------------------------------------------------------------

			except Exception,e:
				print e

class cSetSEFrameUI(Ui_Dialog,QtGui.QDialog):
	def __init__(self, parent=None):
		super(cSetSEFrameUI, self).__init__()
		self.setupUi(self)


class cSetSEFrame(object):
	def __init__(self, parent =None):
		super(cSetSEFrame, self).__init__()
		self.parent = parent
		self.ui = cSetSEFrameUI(self.parent)
		self.sns =  None


		#self.ui.setQPB.clicked.connect(self.set)
		self.ui.accepted.connect(self.set)
		#self.ui.finished.connect(self.q)#貌似是 -关闭- 这个命令执行之前
		self.ui.rejected.connect(self.q)

		self.sns =  nuke.selectedNodes()
		self.ui.show()

	def set(self):
		worker =  proNF3pnode(self.sns)
		worker.setStartEnd(self.ui.sQSB.value(), self.ui.eQSB.value())


	def q(self):
		self.sns = None




def setSE():
	global proObj
	proObj =  cSetSEFrame()

def resetSEEXP():
	sns =  nuke.selectedNodes()
	worker =  proNF3pnode(sns)
	worker.resetStarEndEXP()

def dumpPath():
	sns =  nuke.selectedNodes()
	worker =  proNF3pnode(sns)
	worker.dumpPath()

def setCacheAlways():
	sns =  nuke.selectedNodes()
	worker =  proNF3pnode(sns)
	worker.setCacheAlways()

def setCacheAuto():
	sns =  nuke.selectedNodes()
	worker =  proNF3pnode(sns)
	worker.setCacheAuto()

