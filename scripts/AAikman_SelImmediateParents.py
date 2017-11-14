import maya.cmds as cmds

sel = cmds.ls(sl=True)
cmds.select(cl=True)
for i in sel:
	try:
		cmds.select(cmds.listRelatives(i, p=True), add=True)
	except:
		print 'No parent found for {}'.format(i)

    