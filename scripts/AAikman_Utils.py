import maya.cmds as cmds


def snapTo(par, chi, constrType=3):
	cmds.select(par, r=True)
	cmds.select(chi, add=True)
	constrName = '{}_tempConstraint'.format(chi)
	if constrType == 1:
		# Translation
		cmds.pointConstraint(mo=False, n=constrName)
	elif constrType == 2:
		# Rotation
		cmds.orientConstraint(mo=False, n=constrName)
	elif constrType == 3:
		# Translation and Rotation
		cmds.parentConstraint(mo=False, n=constrName)
	elif constrType == 4:
		# All
		cmds.parentConstraint(mo=False, n=constrName)
		cmds.delete(constrName)
		cmds.scaleConstraint(mo=False, n=constrName)
	else:
		# Scale
		cmds.scaleConstraint(mo=False, n=constrName)

	cmds.delete(constrName)
	cmds.select(cl=True)


def doSnap(snapType = 3):

	sel = cmds.ls(sl=True)
	toSnapTo = sel[0]
	sel.pop(0)

	for i in sel:
		snapTo(toSnapTo, i, snapType)
