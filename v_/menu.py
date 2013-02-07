#****************** time start *****************
cge_debug = globals().get('cge_debug', None)
if cge_debug:
	print '=================timeTest start:',__file__
	import time
	tStart = time.time()
#***********************************************


# V!ctor definitions
toolbar = nuke.menu('Nodes')
VMenu = toolbar.addMenu('V!ctor', icon='V_Victor.png')
VMenu.addCommand('V_CheckMatte', 'nuke.createNode("V_CheckMatte")', icon='V_CheckMatte.png')
VMenu.addCommand('V_IdBuilder', 'nuke.createNode("V_IdBuilder")', icon='V_IdBuilder.png')
VMenu.addCommand('V_IdPackage', 'nuke.createNode("V_IdPackage")', icon='V_IdPackage.png')
VMenu.addCommand('V_IdFilter', 'nuke.createNode("V_IdFilter")', icon='V_IdFilter.png')
VMenu.addCommand('V_ColorRenditionChart', 'nuke.createNode("V_ColorRenditionChart")', icon='V_ColorRenditionChart.png')
VMenu.addCommand('V_ColorTracker', 'nuke.createNode("V_ColorTracker")', icon='V_ColorTracker.png')
VMenu.addCommand('V_CompareView', 'nuke.createNode("V_CompareView")', icon='V_CompareView.png')
VMenu.addCommand('V_Slate', 'nuke.createNode("V_Slate")', icon='V_Slate.png')

#****************** time end *******************
cge_debug = globals().get('cge_debug', None)
if cge_debug:
	tEnd = time.time()
	print '=============================>timeTest:',tEnd-tStart
	print '=============================>file:',__file__
#***********************************************