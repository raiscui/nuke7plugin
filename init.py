
import os
import sys
import nuke
import os.path
syspath = globals().get('syspath', None)

#sys.path.append(os.path.join(syspath, 'PyQt4'))

#***********************************************
global cge_debug
cge_debug = 1
#***********************************************


def timeTest(func):
	from functools import wraps
	cge_debug = globals().get('cge_debug', None)

	@wraps(func)
	def wrapper(*args):
		if cge_debug:
			print '=================timeTest start:',__file__
			import time
			tStart = time.time()
			func(*args)
			tEnd = time.time()
			print '=============================>timeTest:', tEnd - tStart
			print '=============================>file:', __file__
		else:
			func(*args)
	return wrapper


def regPath(x, dirname, filenames):
	# if 'init.py' in filenames:
	nuke.pluginAddPath(dirname)
	print os.path.basename(dirname), '...'
	

timeTest2 = globals().get('timeTest', None)
@timeTest2
def main():
	import shutil
	old_dir1 = r'C:\Program Files\Common Files\Nuke\6.3\plugins\myplug'
	old_dir2 = r'D:\Program Files\Nuke6.3v4\plugins\user'
	old_dir3 = r'C:\Program Files\Common Files\Nuke\7.0\plugins\myplug'
	old_dir4 = r'D:\Program Files\Nuke6.3v4\plugins\user'
	old_dir = [old_dir1, old_dir2, old_dir3, old_dir4]

	for d in old_dir:
		if os.path.exists(d):
			shutil.rmtree(d)

	os.path.walk(syspath, regPath, None)

if __name__ == '__main__':

	main()
