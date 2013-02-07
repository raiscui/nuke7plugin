#****************** time start *****************
cge_debug = globals().get('cge_debug', None)
if cge_debug:
    print '=================timeTest start:',__file__
    import time
    tStart = time.time()
#***********************************************

### nuke.pluginAddPath("./", addToSysPath=False);
import os
import os.path
global syspath

cwd = syspath + '/gizmos'
files = os.listdir(cwd)

fnames = []
dirs = []
for f in files:
    print f
    fsp = os.path.splitext(f)
    if '.gizmo' == fsp[1]:
        fnames.append(fsp[0])
    elif '.' not in f:
        dirs.append(f)

toolbar = nuke.toolbar("Nodes")
GxMenu = toolbar.addMenu('MyTool', icon='Gtool.png')


for n in fnames:
    GxMenu.addCommand(n, 'nuke.createNode("' + n + '")')

for d in dirs:
    GsubMenu = GxMenu.addMenu(d)
    subDirFiles = os.listdir(os.path.join(cwd, d))
    print "sbfile:", subDirFiles
    for subF in subDirFiles:
        subFsp = os.path.splitext(subF)
        GsubMenu.addCommand(subFsp[0], 'nuke.createNode("' + subFsp[0] + '")')


#****************** time end *******************
cge_debug = globals().get('cge_debug', None)
if cge_debug:
    tEnd = time.time()
    print '=============================>timeTest:',tEnd-tStart
    print '=============================>file:',__file__
#***********************************************