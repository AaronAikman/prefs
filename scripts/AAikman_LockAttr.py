import maya.cmds as cmds

sel = cmds.ls(sl=True)

for i in sel:
	# cmds.setAttr( '{}.tx'.format(i), lock=True )
	cmds.setAttr( '{}.ty'.format(i), lock=True )
	# cmds.setAttr( '{}.tz'.format(i), lock=True )
	cmds.setAttr( '{}.rx'.format(i), lock=True )
	cmds.setAttr( '{}.ry'.format(i), lock=True )
	cmds.setAttr( '{}.rz'.format(i), lock=True )
	cmds.setAttr( '{}.sx'.format(i), lock=True )
	cmds.setAttr( '{}.sy'.format(i), lock=True )
	cmds.setAttr( '{}.sz'.format(i), lock=True )

	print 'Processed ' + i

