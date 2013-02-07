def alignNodes( nodes, direction = 'x' ):
	'''
	Align nodes either horizontally or vertically.
	'''
	if len( nodes ) < 2:
		return
	if direction.lower() not in ('x', 'y'):
		raise ValueError, 'direction argument must be x or y'

	positions = [ float( n[ direction.lower()+'pos' ].value() ) for n in nodes]
	avrg = sum( positions ) / len( positions )
	for n in nodes:
		if direction == 'x':
			n.setXpos( int(avrg) )
		else:
			n.setYpos( int(avrg) )

	return avrg

def ylistNodes( nodes):
	'''
	Align nodes either horizontally or vertically.
	'''
	if len( nodes ) < 2:
		return
	
	
	px = float( nodes[-1][ 'xpos' ].value() )
	py = float( nodes[0][ 'ypos' ].value() )

	for n in nodes:
		n.setXpos( int(px) )
		n.setYpos( int(py) )
		py+=168
