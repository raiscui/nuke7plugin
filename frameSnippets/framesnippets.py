class frameSnippetsPanel(nukescripts.PythonPanel):
	def __init__(self):
		nukescripts.PythonPanel.__init__(self, 'frameSnippets', 'com.ohufx.frameSnippets')
		# CREATE KNOBS

		self.setSnip = nuke.PyScript_Knob('记录当前帧', '记录当前帧')

		self.o = nuke.Boolean_Knob('删除模式')
		# ADD KNOBS
		self.addKnob(self.o)
		self.addKnob(self.update)
		self.frameButtons ={}
		self.cont =0

	def knobChanged(self, knob):
		#print knob.name()
		if knob is self.setSnip:
			self.cont = nuke.activeViewer().node().knob('frame').value()
			vName = nuke.activeViewer().node().name()
			b = nuke.PyScript_Knob(str(self.cont),vName + str(self.cont))
			self.addKnob(b)
			self.frameButtons[b] = vName


			self.cont = self.cont+1

		elif knob in self.frameButtons.keys():
			if self.o.value():
				#del model
				print 'del'
				self.removeKnob(knob)
				self.frameButtons.pop(knob)
			else:
				print 'go',knob.name()


def addframeSnippetsPanel():
	global fsPanel
	fsPanel = frameSnippetsPanel()
	return fsPanel.addToPane()

paneMenu = nuke.menu('Pane')
paneMenu.addCommand('frameSnippets', addframeSnippetsPanel)
nukescripts.registerPanel('com.ohufx.frameSnippets', addframeSnippetsPanel)