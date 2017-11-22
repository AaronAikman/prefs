'''
Author:
Aaron Aikman

Date of Creation:
11/20/2017

Installation:
Put in scripts folder

Shelf Button:
import AAikman_GroupUnder as aagu
reload(aagu)
aagu.main()

'''

import maya.cmds as cmds

sel = cmds.ls(sl=True)
newGroups = []

def main():
	for i in sel:
		cmds.select(i, r=True)
		pivLocFull = cmds.xform(q=True, piv=True, a=True)
		# print pivLoc
		if i.endswith('_offsetgrp'):
			cmds.pickWalk( direction='down' )
			i = cmds.ls(sl=True)[0]
			grpName ='{}_drivengrp'.format(i)
		elif i.endswith('_drivengrp'):
			grpName ='{}_drivenparentgrp'.format(i[:-10])
		else:
			grpName ='{}_offsetgrp'.format(i)
		if cmds.objExists(grpName):
			grpName += '_1'
		newGroups.append(grpName)
		cmds.group(n=grpName)
		cmds.select(grpName, r=True)
		pivLoc = [pivLocFull[0], pivLocFull[1], pivLocFull[2]]
		cmds.xform(piv=pivLoc)
	cmds.select(newGroups, r=True)

# main()