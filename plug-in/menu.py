#****************** time start *****************
cge_debug = globals().get('cge_debug', None)
if cge_debug:
	print '=================timeTest start:',__file__
	import time
	tStart = time.time()
#***********************************************

toolbar = nuke.menu("Nodes")
myplugs = toolbar.addMenu("Myplug")


# myplugs.addCommand("GeoPoints", "nuke.createNode(\"GeoPoints\")")

# myplugs.addCommand("lGlass", "nuke.createNode(\"lGlass\")")

# myplugs.addCommand("ImageTool", "nuke.createNode(\"ImageTool\")")

# myplugs.addCommand("Rank", "nuke.createNode(\"Rank\")")

myplugs.addCommand("Detail", "nuke.createNode(\"Detail\")")

# myplugs.addCommand("ReflectionCard", "nuke.createNode(\"ReflectionCard\")")

# myplugs.addCommand("ReflectMat", "nuke.createNode(\"ReflectMat\")")

# myplugs.addCommand("CrankItUp", "nuke.createNode(\"CrankItUp\")")

# myplugs.addCommand("IGamma", "nuke.createNode(\"IGamma\")")

#****************** time end *******************
cge_debug = globals().get('cge_debug', None)
if cge_debug:
	tEnd = time.time()
	print '=============================>timeTest:',tEnd-tStart
	print '=============================>file:',__file__
#***********************************************