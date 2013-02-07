'''
	====================================
	CREATOGETHER forEach Node for Nuke
	====================================

	Created by Dan Borufka 2011
	http://www.creatogether.com
	Version 1.0

'''

import nuke

def forEach():
	forbidden = ['RotoPaint','Roto'];

	for n in nuke.selectedNodes():
		feMsg = 'Nodes from type ' + n.Class() + ' are not supported yet. Please remove them from the selection before creating the ForEach node.';
		if n.Class() in forbidden:
			nuke.message(feMsg);
			return False;
			
	feGroup = nuke.collapseToGroup();
	feGroup.setName("forEach");
	
	for n in feGroup.nodes():
	    n.setSelected(False);
	nuke.allNodes("Input", feGroup)[0].setSelected(True);
	
	feTab = feGroup.addKnob(nuke.Tab_Knob("forEach"));
	feGroup.addKnob(nuke.Int_Knob("n_inputs", "number of inputs"));
	feGroup.addKnob(nuke.Boolean_Knob("manual", "manual loop"));
	feGroup.addKnob(nuke.Int_Knob("init", "from:"));
	feGroup.addKnob(nuke.Int_Knob("end", "to:"));
	feGroup['n_inputs'].setValue(1);
	feGroup['n_inputs'].setTooltip("determines the number of inputs (arrows) the node has got.");
	feGroup["manual"].setTooltip("If in manual mode forEach will run from init to end.");
	feGroup["init"].setTooltip("The init value of the loop. In pseudocode, this would correspond to for(i=init; i<=end; i++)");
	feGroup["end"].setTooltip("The end value of the loop. In pseudocode, this would correspond to for(i=init; i<=end; i++)");
	feGroup["end"].setValue(10);
	feGroup["manual"].setFlag(nuke.STARTLINE);
	feGroup["init"].clearFlag(nuke.STARTLINE); feGroup["init"].setEnabled(False);
	feGroup["end"].clearFlag(nuke.STARTLINE); feGroup["end"].setEnabled(False);
	feGroup.knob("knobChanged").setValue("with nuke.thisNode():\n    knob = nuke.thisKnob();\n    if(knob.name() == 'n_inputs'):\n        n_inps = len(nuke.allNodes('Input'));\n        n_knob = int(float(knob.value()))-1;\n\n        if n_knob != n_inps:\n            for i in range(n_inps-1, n_knob, cmp(n_knob, n_inps)):\n                if(n_inps < n_knob):\n                    nuke.nodes.Input();\n                elif n_knob > -1:\n                    nuke.delete(nuke.allNodes('Input')[0]);\n    elif(knob.name() == 'manual'):\n        nuke.thisNode()['init'].setEnabled(knob.value());\n        nuke.thisNode()['end'].setEnabled(knob.value());");
	
	feGroup.addKnob(nuke.PyScript_Knob("run_btn", "explode loop"));
	feGroup['run_btn'].setTooltip("transforms the forEach group into clones created by the loop.");
	feGroup['run_btn'].setCommand("from types import *\n\ndef is_numeric(n):\n    try: \n        float(n);\n        return True;\n    except TypeError:\n        return False;\n\nfeGroup = nuke.thisNode();\nfePadding = feGroup.knob('padd').getValue();\nfeCY = int(feGroup.ypos() + feGroup.screenHeight()/2);\nfeCX = int(feGroup.xpos() + feGroup.screenWidth()/2);\nfeW = 0; feH = 0;\nfe_horiz = (feGroup.knob('layout').value() == 'horizontal');\n\nfe_manual = feGroup['manual'].value();\n\nfeInputs_num = feGroup.inputs() if not fe_manual else (int(feGroup['end'].value()) - int(feGroup['init'].value()));\nfeInputs = feGroup.dependencies();\nfeInputs.sort(lambda a,b: cmp(a.xpos() if fe_horiz else a.ypos(), b.xpos() if fe_horiz else b.ypos()));\n\nif fe_manual: feInputs += [fakeInp for fakeInp in xrange(feInputs_num - len(feInputs))];\n\n#expand group:\nfeGroup = feGroup.expand();\n\n#create a clone for every input\nfor i, feInput in enumerate(feInputs):\n    if i>0: nuke.cloneSelected();\n\n    feGroup = nuke.selectedNodes();\n\n    feEach = nuke.nodes.NoOp();\n    feEach.setName('each');\n    \n    feI = nuke.String_Knob('i', 'instance #');\n    feEach.addKnob(feI);\n    feI.setValue(str(i));\n    feI.setTooltip('Use [python {forEach_i()}] inside an expression of a node created by the forEach node to access the iterator of the for loop (i). For this to work you need to keep the each-nodes.');\n    feI.setEnabled(False);\n    \n    # find first node:\n    for feC in feGroup:\n        if feC.isSelected():\n            feClone = feC;\n        else:\n            break;\n    \n    if feClone.maxInputs > 0: feClone.setInput(0, feEach);\n\n    if not fe_manual or not is_numeric(feInput): feEach.setInput(0, feInput);\n    if fe_horiz: \n        feEach.setYpos(feCY);\n    else:\n        feEach.setXpos(feCX);\n\n    feEach.setSelected(True);\n    feGroup = nuke.selectedNodes();\n    \n    for j,node in enumerate(feGroup):       #walk thru all nodes within & position\n        if fe_horiz:\n            feW = max(feW, node.screenWidth() + fePadding);\n        else:\n            feH = max(feH, node.screenHeight() + fePadding);\n\n        if fe_horiz: \n            node.setXpos(int(feCX - feW * (feInputs_num/2) + feW * i));\n        else: \n            node.setYpos(int(feCY - feH * (feInputs_num/2) + feH * i));\n    feEach.setYpos(feClone.ypos()-feClone.screenHeight()-feEach.screenHeight()-40);\n    feEach.setSelected(False);\n\n#clean up\nnuke.selectAll();\nnuke.invertSelection();\n\n#i-function\ndef forEach_i():\n    n = nuke.thisNode();\n    if n.name() != 'Root':\n        while (n.Class() != 'NoOp' or not n.name().startswith('each')) and len(n.dependencies()) > 0:\n            n = n.dependencies()[0];\n        return int(n['i'].value()) if n.knob('i') != None else -1;\n    else:\n        return -1;");
	feGroup['run_btn'].setFlag(nuke.STARTLINE);
	feGroup.addKnob(nuke.Tab_Knob("display", "display options"));
	feGroup.addKnob(nuke.Enumeration_Knob("layout", "preferred layout", ["horizontal", "vertical"]));
	feGroup.addKnob(nuke.Double_Knob("padd", "padding"));
	feGroup['padd'].setTooltip("determines the space between branches.");
	feGroup['padd'].setValue(300);
	return True;
	
nuke.menu('Nodes').addMenu('Creatogether', icon='creatogether.png');
nuke.menu('Nodes').addCommand('Creatogether/ForEach', "forEach.forEach()", icon='ctg_forEach.png');