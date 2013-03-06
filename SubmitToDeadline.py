import os, sys
import nuke, nukescripts
from subprocess import Popen,PIPE

def main():
	# Get the repository root
	stdout = None
	if os.path.exists( "/Applications/Deadline/Resources/bin/deadlinecommand" ):
		stdout = os.popen( "/Applications/Deadline/Resources/bin/deadlinecommand GetRepositoryRoot" )
	elif os.path.exists("/usr/local/Prime_Focus/Deadline/bin/deadlinecommand"):
		stdout = Popen(("/usr/local/Prime_Focus/Deadline/bin/deadlinecommand","GetRepositoryRoot"),stdout=PIPE ).stdout
	else:
		stdout = os.popen("deadlinecommand GetRepositoryRoot" )
	path = stdout.read()
	path += "/submission/Nuke"
	path = path.replace("\n","").replace( "\\", "/" )
	stdout.close()

	# Add the path to the system path
	print "Appending \"" + path + "\" to system path to import SubmitNukeToDeadline module"
	sys.path.append( path )

	# Import the script and call the main() function
	import SubmitNukeToDeadline
	SubmitNukeToDeadline.SubmitToDeadline( path )