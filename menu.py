# -*- coding:utf-8 -*-
#****************** time start *****************
cge_debug = globals().get('cge_debug', None)
if cge_debug:
	print '=================timeTest start:',__file__
	import time
	tStart = time.time()
#***********************************************
# -*- coding: UTF-8 -*-
# coding=utf-8
import SearchReplacePanel

def addSRPanel():
        '''Run the panel script and add it as a tab into the pane it is called from'''
        myPanel = SearchReplacePanel.SearchReplacePanel()
        return myPanel.addToPane()
 
#THIS LINE WILL ADD THE NEW ENTRY TO THE PANE MENU
nuke.menu('Pane').addCommand('SearchReplace', addSRPanel)
 
#THIS LINE WILL REGISTER THE PANEL SO IT CAN BE RESTORED WITH LAYOUTS
nukescripts.registerPanel('com.ohufx.SearchReplace', addSRPanel)



#Align a bunch of Nodes either horizontally or vertically in the DAG
import alignNodes
menuBar = nuke.menu("Nuke")
menuBar.addCommand('Edit/Node/Align/horizontally', 'alignNodes.alignNodes( nuke.selectedNodes(), direction="x" )', 'alt+x')
menuBar.addCommand('Edit/Node/Align/vertically', 'alignNodes.alignNodes( nuke.selectedNodes(), direction="y" )', 'alt+y')
menuBar.addCommand('Edit/Node/Align/verticallysort', 'alignNodes.ylistNodes( nuke.selectedNodes() )', 'ctrl+l')


nuke.load('vrayCameraAttributes.py')

from framesnippets2 import frameSnippetsPanel
#=============------------   Prometeus SYSTEM ------------ =============#

from proNuke import pro_wp
menuBar.addCommand('Prometeus/设置3屏节点/开始结束帧','pro_wp.setSE()')
menuBar.addCommand('Prometeus/设置3屏节点/重置帧表达式','pro_wp.resetSEEXP()')
menuBar.addCommand('Prometeus/设置3屏节点/塌陷路径','pro_wp.dumpPath()')
menuBar.addCommand('Prometeus/设置3屏节点/设置本地缓存always','pro_wp.setCacheAlways()')
import SubmitToDeadline
menuBar.addCommand('Prometeus/发送到Deadline','SubmitToDeadline.main()')

#****************** time end *******************
cge_debug = globals().get('cge_debug', None)
if cge_debug:
	tEnd = time.time()
	print '=============================>timeTest:',tEnd-tStart
	print '=============================>file:',__file__
else:
	print 'no debug'
#***********************************************