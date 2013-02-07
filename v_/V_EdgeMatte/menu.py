#****************** time start *****************
cge_debug = globals().get('cge_debug', None)
if cge_debug:
	print '=================timeTest start:',__file__
	import time
	tStart = time.time()
#***********************************************

# V_EdgeMatte definitions
toolbar = nuke.menu('Nodes')
VMenu = toolbar.addMenu('V!ctor', icon='V_Victor.png')
VMenu.addCommand('V_EdgeMatte', 'nuke.createNode("V_EdgeMatte")', icon='V_EdgeMatte.png')

#****************** time end *******************
cge_debug = globals().get('cge_debug', None)
if cge_debug:
	tEnd = time.time()
	print '=============================>timeTest:',tEnd-tStart
	print '=============================>file:',__file__
#***********************************************