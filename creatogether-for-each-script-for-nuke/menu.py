#****************** time start *****************
cge_debug = globals().get('cge_debug', None)
if cge_debug:
	print '=================timeTest start:',__file__
	import time
	tStart = time.time()
#***********************************************


import forEach


#****************** time end *******************
cge_debug = globals().get('cge_debug', None)
if cge_debug:
	tEnd = time.time()
	print '=============================>timeTest:',tEnd-tStart
	print '=============================>file:',__file__
#***********************************************