Pixelfudger for Nuke

TO INSTALL:

If you don't have an init.py or menu.py in ~/.nuke:

	copy these files in ~/.nuke
	- init.py
	- menu.py
	- pixelfudger


If you have a custom init.py and menu.py already:

	- copy pixelfudger/ to ~/.nuke
	- add this line to init.py:
		nuke.pluginAddPath('pixelfudger')
		
	- add this line to menu.py:
		import pixelfudger
		
After a Nuke restart, you should have the Pixelfuger menu in your toolbar.

LICENCE:

You are free to use Pixelfudger gizmos for personal and commercial use as
long as you leave the credit text intact in the source files and in the 
gizmo's knobs.

AUTHOR:
Xavier Bourque
xbourque@gmail.com
www.pixelfudger.com
© 2012