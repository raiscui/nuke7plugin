
#========================================================
#更改文件路径
#========================================================
sns =  nuke.selectedNodes()
for sn in sns:
	try:
		snfile = sn.knob('file')
		filepath= snfile.value()
		# = filepath.replace('[knob sourcepath.label]' ,'[value root.name]')
		filepath = filepath.replace(r'//10.0.0.16/net-render/cuiluming/render_in/cjchukou_Project/images/cj1_sec_v_in_render_output_L%v_DMG_B_cam_stereoCamera%V1' ,'[knob sourcepath.label]')
		filepath = filepath.replace(r'//10.0.0.16/net-render/cuiluming/render_in/cjchukou_Project/images/cj1_sec_v_in_render_output_M%v_stereoCamera%V' ,'[knob sourcepath1.label]')
		filepath = filepath.replace(r'//10.0.0.16/net-render/cuiluming/render_in/cjchukou_Project/images/cj1_sec_v_in_render_output_R%v_DMG_B_cam_stereoCamera%V2' ,'[knob sourcepath2.label]')
		#filepath = filepath.replace('.exr' ,'.%04d.exr')
		snfile.setValue(filepath)
	except:
		pass

sns =  nuke.selectedNodes()
for sn in sns:
	try:
		snfile = sn.knob('file')
		filepath= snfile.value()
		# = filepath.replace('[knob sourcepath.label]' ,'[value root.name]')
		filepath = filepath.replace('Right' ,'%V')
		filepath = filepath.replace('Left' ,'%V')

		filepath = filepath.replace('_LL_' ,'_L%v_')
		filepath = filepath.replace('_LR_' ,'_L%v_')
		filepath = filepath.replace('_ML_' ,'_M%v_')
		filepath = filepath.replace('_MR_' ,'_M%v_')
		filepath = filepath.replace('_RL_' ,'_R%v_')
		filepath = filepath.replace('_RR_' ,'_R%v_')

		#filepath = filepath.replace('.exr' ,'.%04d.exr')
		snfile.setValue(filepath)
	except:
		pass



#========================================================
#更改文件路径
#========================================================
sns =  nuke.selectedNodes()
for sn in sns:
	try:
		s = sn.knob('last')
		#sv =nuke.toNode('root').knob('e').value()
		sv = "[value root.e]"
		if sv == 3230:
			print sn.name()

	except:
		pass



sns =  nuke.selectedNodes()
for sn in sns:
	try:
		f = sn.knob('first')
		#fv =nuke.toNode('root').knob('s').value()
		fv = "[value root.s]"
		#f.setValue(int(fv))
		f.setExpression(fv)

		s = sn.knob('last')
		#sv =nuke.toNode('root').knob('e').value()
		sv = "[value root.e]"
		#s.setValue(int(sv))
		s.setExpression(sv)

		of = sn.knob('origfirst')
		ofv ="[value root.s]"
		of.setExpression(ofv)

		os = sn.knob('origlast')
		osv ="[value root.e]"
		os.setExpression(osv)
		sn.knob('format').setValue('hd1080')
	except:
		pass
for sn in sns:
	try:
		sn.knob('after').setValue(3)
		sn.knob('before').setValue(3)
	except:
		pass


def setSE(ss,ee):
	sns =  nuke.selectedNodes()
	for sn in sns:
		try:
			f = sn.knob('first')
			#fv =nuke.toNode('root').knob('s').value()
			fv = ss
			f.setValue(int(fv))
			#f.setExpression(fv)

			s = sn.knob('last')
			#sv =nuke.toNode('root').knob('e').value()
			sv = ee
			s.setValue(int(sv))
			#s.setExpression(sv)

			of = sn.knob('origfirst')
			ofv =ss
			of.setValue(int(ofv))

			os = sn.knob('origlast')
			osv =ee
			os.setValue(int(osv))
			sn.knob('format').setValue('slsj3p')
		except:
			pass
	for sn in sns:
		try:
			sn.knob('after').setValue(3)
			sn.knob('before').setValue(3)
		except:
			pass
setSE(600,2290)






#========================================================
#只修改 开始结束贞
#========================================================
sns =  nuke.selectedNodes()
for sn in sns:
	try:
		f = sn.knob('first')
		fv= f.value()
		fv =nuke.toNode('root').knob('s').value()
		f.setValue(int(fv))

		s = sn.knob('last')
		sv= s.value()
		sv =nuke.toNode('root').knob('e').value()
		s.setValue(int(sv))


		sn.knob('format').setValue('hd1080')
	except:
		pass



#========================================================
#删除
#========================================================
sns =  nuke.selectedNodes()
for sn in sns:
	try:
		snfile = sn.knob('file')
		filepath= snfile.value()
		if 'ML' not in filepath and 'ml' not in filepath:
			nuke.delete(sn)

	except:
		pass


#========================================================
#3P节点修改
#========================================================
def set3pSE(ss,ee):
	sns =  nuke.selectedNodes()
	for sn in sns:
		try:
			f = sn.node('Read39').knob('first')
			#fv =nuke.toNode('root').knob('s').value()
			fv = ss
			f.setValue(int(fv))
			#f.setExpression(fv)

			s = sn.node('Read39').knob('last')
			#sv =nuke.toNode('root').knob('e').value()
			sv = ee
			s.setValue(int(sv))
			#s.setExpression(sv)

			of = sn.node('Read39').knob('origfirst')
			ofv =ss
			of.setValue(int(ofv))

			os = sn.node('Read39').knob('origlast')
			osv =ee
			os.setValue(int(osv))

		except:
			pass
	for sn in sns:
		try:
			sn.node('Read39').knob('after').setValue(3)
			sn.node('Read39').knob('before').setValue(3)
		except:
			pass
set3pSE(260, 1500)




def set3pfile():
	sns =  nuke.selectedNodes()
	for sn in sns:
		try:
			f = sn.node('Read39').knob('file')
			#fv =nuke.toNode('root').knob('s').value()
			fv = '''[knob [knob parent.rootp].label]/[python {nuke.thisParent().knob('c2').value()+'/' if nuke.thisParent().knob('path_cam').value() else ''}][python {nuke.thisParent().knob('pass').value()+'/' if nuke.thisParent().knob('havepassdir').value() and nuke.thisParent().knob('pass').value() != '' else ''}][knob parent.fname][python {nuke.thisParent().knob('c2').value() if nuke.thisParent().knob('name_cam').value() else ''}][python {'.'+nuke.thisParent().knob('pass').value() if nuke.thisParent().knob('havenamepass').value() and nuke.thisParent().knob('pass').value() != '' else ''}][knob parent.ext]'''
			f.setValue((fv))
			#f.setExpression(fv)


			of = sn.node('Read1').knob('file')
			ofv = '''[knob [knob parent.rootp].label]/[python {nuke.thisParent().knob('c1').value()+'/' if nuke.thisParent().knob('path_cam').value() else ''}][python {nuke.thisParent().knob('pass').value()+'/' if nuke.thisParent().knob('havepassdir').value() and nuke.thisParent().knob('pass').value() != '' else ''}][knob parent.fname][python {nuke.thisParent().knob('c1').value() if nuke.thisParent().knob('name_cam').value() else ''}][python {'.'+nuke.thisParent().knob('pass').value() if nuke.thisParent().knob('havenamepass').value() and nuke.thisParent().knob('pass').value() != '' else ''}][knob parent.ext]'''
			of.setValue((ofv))

			os = sn.node('Read3').knob('file')
			osv = '''[knob [knob parent.rootp].label]/[python {nuke.thisParent().knob('c3').value()+'/' if nuke.thisParent().knob('path_cam').value() else ''}][python {nuke.thisParent().knob('pass').value()+'/' if nuke.thisParent().knob('havepassdir').value() and nuke.thisParent().knob('pass').value() != '' else ''}][knob parent.fname][python {nuke.thisParent().knob('c3').value() if nuke.thisParent().knob('name_cam').value() else ''}][python {'.'+nuke.thisParent().knob('pass').value() if nuke.thisParent().knob('havenamepass').value() and nuke.thisParent().knob('pass').value() != '' else ''}][knob parent.ext]'''
			os.setValue((osv))

		except:
			pass

set3pfile()





#=============------------  移除pass里不要的 /  ------------ =============#


	
def removePassWord():
	sns =  nuke.selectedNodes()
	for sn in sns:
		try:
			f = sn.knob('pass')
			fv = f.value().replace('/', '')
			f.setValue((fv))
		except:
			pass

removePassWord()
