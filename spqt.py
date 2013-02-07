"""
Encapsulate what's needed to run (multiple) PyQt widgets in Nuke.
Run a QApplication (and its event loop) in another thread,
    and provide a system for forwarding (by Qt signal) callables
    to that thread for execution.

Define convenience functions that wrap Nuke's calls
to execute Nuke API calls in the main thread.

To use (and run the example node lister widget):
    $ env NUKE_PATH=/path/to/.../directoryWithSpqt/ nuke
    >>> import spqt
    >>> spqt.CreateNodeLister() # call several times for multiple widgets
    Create nodes and see the widgets update, click on the widgets
        to have them call Nuke Python API functions.
"""
from __future__ import with_statement
#import pyqt
#if not pyqt.requiredVersion():
    #pyqt.require('4.4.3')
import PyQt4
from PyQt4 import QtGui, QtCore
import nuke, threading, logging, atexit

log = logging.getLogger('SpQt')



###
# SpQt: manage the QApplication and communicating callables to it.

global qtThread
global qappCreationEvent

qtThread = None
qappCreationEvent = threading.Event()

global callableQueue
global callableQueueSemaphore
callableQueue = []
callableQueueSemaphore = None # assign after defining SemaphoreGuard



def QtRun(callable, *args, **kwargs):
    """
    Run a callable with arbitrary (kw)args in a separate thread,
        with the QApplication.
    """
    global callableQueueSemaphore
    _StartQtThread()
    with callableQueueSemaphore:
        callableQueue.append((callable, args, kwargs))


def _RunQueuedCallables():
    """Check for and run a queued callable in the QApplication's thread."""
    global callableQueueSemaphore
    nextQueued = None

    with callableQueueSemaphore:
        if callableQueue:
            nextQueued = callableQueue.pop()

    if nextQueued:
        callable, args, kwargs = nextQueued
        try:
            callable(*args, **kwargs)
        except:
            log.error('running command for Qt:', exc_info=True)


def _StartQtThread():
    """Ensure that the thread for the QApplication is running."""
    global qtThread
    if qtThread:
        return

    global qappCreationEvent

    log.debug('Creating thread for QApplication.')
    qtThread = threading.Thread(target=_RunQtApp)
    qtThread.start()
    qappCreationEvent.wait()
    log.debug('QApplication created, ready for main thread execution.')


def _CloseQtThread():
    """Clean up on exit (avoid crash-on-exit)."""
    global qtThread
    if not qtThread:
        return
    QtRun(QtCore.QCoreApplication.quit)
    qtThread.join()
atexit.register(_CloseQtThread)


def _RunQtApp():
    """
    Main method for the thread: create a QApplication and call exec_().
    This also creates a _CommandReciever, which listens for signals
        from the sender, allowing the thread to pick up new commands
        while exec_() is running.
    """
    global qappCreationEvent

    log.debug('creating new QApplication')
    app = QtGui.qApp
    app.setStyle('DarkMojo')
    app.setQuitOnLastWindowClosed(False)
    qappCreationEvent.set()

    t = QtCore.QTimer()
    t.setSingleShot(False)
    t.setInterval(200)
    QtCore.QObject.connect(t, QtCore.SIGNAL('timeout()'), _RunQueuedCallables)
    t.start()

    r = app.exec_()
    log.debug('exec_() returned %d' % r)



###
# NodeLister example

import random
class NodeLister(QtGui.QPushButton):
    """
    Qt-in-Nuke demo widget: list created nodes,
    and on click do something to them.
    """
    def __init__(self):
        QtGui.QPushButton.__init__(self, None)
        for node in ExecuteInMainThread(nuke.allNodes):
            self.__appendNodeName(node.name())

        ExecuteInMainThread(nuke.addOnCreate, self.__onCreateCallback)

        QtCore.QObject.connect(self, QtCore.SIGNAL('clicked()'), self.__clicked)


    def __onCreateCallback(self):
        node = ExecuteInMainThread(nuke.thisNode)
        self.__appendNodeName(node.name())


    def __appendNodeName(self, name):
        t = str(self.text())
        if t:
            t += ', '
        t += name
        self.setText(t)


    def __clicked(self):
        log.debug('clicked')
        nodes = []
        nodeNames = [n.strip() for n in str(self.text()).split(',')]
        for name in nodeNames:
            node = ExecuteInMainThread(nuke.toNode, name)
            if node:
                log.debug('processing node %s' % node.name())
                nodes.append(node)
            else:
                log.debug("no node named '%s'" % name)

        r, g, b = random.random(), random.random(), random.random()
        packed = GetColorFromRgbF(r, g, b)
        log.debug('color is (%.2f, %.2f, %.2f) --> %d' % (r, g, b, packed))
        for node in nodes:
            log.debug('set tile color for %s' % (node.name(),))
            ExecuteInMainThread(node['tile_color'].setValue, packed)


global widgets
widgets = []
def CreateNodeLister():
    """Qt-in-Nuke demo: create a demo widget."""
    def makeAndStoreLabel():
        global labels
        l = NodeLister()
        l.show()
        widgets.append(l)

    QtRun(makeAndStoreLabel)



###
# SpThreadUtil: (thinly) wrap nuke.executeInMain,
#   make a context guard for threading module semaphores

global mainThread
mainThread = threading.currentThread()


def ExecuteInMainThread(callable, *args, **kwargs):
    """
    Wrap nuke.executeInMain.executeInMainThreadWithResult .
    (Calling this from the main thread will cause the GUI to lock.)
    """
    return nuke.executeInMain.executeInMainThreadWithResult(callable, args, kwargs)


def ExecuteInMainThreadFromAny(callable, *args, **kwargs):
    """
    Wrap nuke.executeInMain.executeInMainThreadWithResult ,
    but check whether this is being called in the main thread
    and if so make the call directly instead.
    """
    global mainThread
    if threading.currentThread() == mainThread:
        return callable(*args, **kwargs)
    else:
        return nuke.executeInMain.executeInMainThreadWithResult(callable, args, kwargs)


def ExecuteInMainThreadNonblocking(callable, *args, **kwargs):
    """
    Wrap nuke.executeInMain.executeInMainThread.
    (Calling this from the main thread will cause the GUI to lock.)
    """
    return nuke.executeInMain.executeInMainThread(callable, args, kwargs)


def ExecuteInMainThreadNonblockingFromAny(callable, *args, **kwargs):
    """
    Wrap nuke.executeInMain.executeInMainThread ,
    but check whether this is being called in the main thread
    and if so make the call directly instead (in which case it is blocking).
    """
    global mainThread
    if threading.currentThread() == mainThread:
        callable(*args, **kwargs)
    else:
        nuke.executeInMain.executeInMainThread(callable, args, kwargs)



class SemaphoreGuard(object):
    """Wrap threading.Semaphore acquire/release in a context guard."""
    def __init__(self, n=1):
        self.__semaphore = threading.Semaphore(n)
    def __enter__(self):
        self.__semaphore.acquire()
    def __exit__(self, e, v, tb):
        self.__semaphore.release()



###
# SpKnobDefaults: utility functions for Nuke UI colors

COLOR_BITS = 8
def GetColorFromRgbF(r, g, b, a=0.0):
    """
    From the nuke.getColor docstring: The format of the color values is
    packed 8bit rgb multiplied by 256 (ie in binary: 0xRRGGBB00).
    """
    multiplier = (1 << COLOR_BITS) - 1
    outColor = 0
    first = True
    for component in (r, g, b, a):
        if first:
            first = False
        else:
            outColor = outColor << COLOR_BITS
        outColor += int(max(0.0, min(1.0, component))*multiplier)
    return outColor


def GetRgbFFromColor(inColor):
    """@see GetColorFromRgbF)"""
    if type(inColor) not in (int, long):
        raise ValueError('input color must be an int or long')
    colorBitfield = inColor
    components = []
    mask = (1 << COLOR_BITS) - 1
    for i in xrange(4):
        c = (colorBitfield & mask)
        components.insert(0, float(c)/mask)
        colorBitfield = colorBitfield >> COLOR_BITS
    return components



callableQueueSemaphore = SemaphoreGuard()

