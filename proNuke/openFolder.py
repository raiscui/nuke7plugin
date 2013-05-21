#!/usr/bin/env python
#coding:utf-8
# Author:  rais --<CGE>
# Purpose: select file node , run do(), then open the folder
# Created: 2013/5/13

import sys
import nukescripts.openurl as openurl
import nuke
import os.path
#----------------------------------------------------------------------
def do():
	"""main"""
	sns =  nuke.selectedNodes()
	for sn in sns:
		filepath = nuke.filename(sn)
		if filepath is not None:
			filepath = 'file:' + os.path.dirname(filepath)
			currentView = nuke.activeViewer().view()
			filepath = filepath.replace(r'%v', currentView[0])
			filepath = filepath.replace(r'%V', currentView)
			print filepath
			openurl.start(filepath)
