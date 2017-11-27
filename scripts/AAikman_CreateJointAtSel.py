'''
Author:
Aaron Aikman

Date of Creation:
11/21/2017

Installation:
Put in scripts folder

Shelf Button:
import AAikman_CreateJointAtSel as aajs
reload(aajs)
aajs.main()

Marking Menu Script:
python( "import AAikman_CreateJointAtSel as aajs; reload(aajs); aajs.main;")

'''

import maya.cmds as cmds

def main():
	sel = cmds.ls(sl=True)
	jointPrev = ''
	for link in sel:
	    cmds.select(link, r=True)
	    loc = cmds.xform(q=True, t=True, ws=True)
	    cmds.select(cl=True)
	    if jointPrev:
	        cmds.select(jointPrev)
	    jointPrev = cmds.joint()
	    cmds.move(loc[0], loc[1], loc[2])