
 #This code is used by the Relight, EnvRelight and ReProject3D gizmos to read metadata from OpenEXR files.


def exrCam():
	def getMetadataMatrix(meta_list):
		m = nuke.math.Matrix4()
		try:
			for i in range(0, 16):
				m[i] = meta_list[i]
		except:
			m.makeIdentity()
		return m

	n = nuke.thisNode()

	hold = int(n['frameHold'].value())

	camMatrix = getMetadataMatrix(n.metadata('exr/worldToCamera', hold))

	flipZ = nuke.math.Matrix4()
	flipZ.makeIdentity()
	flipZ.scale(1, 1, -1)

	transposedMatrix = nuke.math.Matrix4(camMatrix)
	transposedMatrix.transpose()
	transposedMatrix = transposedMatrix * flipZ
	invMatrix = transposedMatrix.inverse()

	n['matrix'].setValue(invMatrix[0], 0)
	n['matrix'].setValue(invMatrix[1], 1)
	n['matrix'].setValue(invMatrix[2], 2)
	n['matrix'].setValue(invMatrix[3], 3)
	n['matrix'].setValue(invMatrix[4], 4)
	n['matrix'].setValue(invMatrix[5], 5)
	n['matrix'].setValue(invMatrix[6], 6)
	n['matrix'].setValue(invMatrix[7], 7)
	n['matrix'].setValue(invMatrix[8], 8)
	n['matrix'].setValue(invMatrix[9], 9)
	n['matrix'].setValue(invMatrix[10], 10)
	n['matrix'].setValue(invMatrix[11], 11)
	n['matrix'].setValue(invMatrix[12], 12)
	n['matrix'].setValue(invMatrix[13], 13)
	n['matrix'].setValue(invMatrix[14], 14)
	n['matrix'].setValue(invMatrix[15], 15)
	return
