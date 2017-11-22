'''
Author:
Aaron Aikman

Date of Creation:
11/20/2017

Installation:
Put in scripts folder

Shelf Button:
import AAikman_UnlockVis as aauv
reload(aauv)
aauv.main()

'''

import maya.cmds as cmds

sel = cmds.ls(sl=True)

def main():
	for i in sel:
		cmds.select(i, r=True)
		# pivLocFull = cmds.xform(q=True, piv=True, a=True)
		# print pivLoc
		visName ='{}.visibility'.format(i)
		cmds.setAttr(visName, l=False)
	cmds.select(sel, r=True)

# main()