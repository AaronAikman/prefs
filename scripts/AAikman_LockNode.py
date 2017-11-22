'''
Author:
Aaron Aikman

Date of Creation:
11/20/2017

Installation:
Put in scripts folder

Shelf Button:
import AAikman_LockNode as aaln
reload(aaln)
aaln.main(0)

'''

import maya.cmds as cmds

sel = cmds.ls(sl=True)
def main(lockMode=1):
	for i in sel:
		cmds.select(i, r=True)
		cmds.lockNode(l=lockMode)
	cmds.select(sel, r=True)

