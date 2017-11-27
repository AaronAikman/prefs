'''
Author:
Aaron Aikman

Date of Creation:
11/21/2017

Installation:
Put in scripts folder
Enter 'rehash' in the mel command line
Put the Shelf Button script into a python button

Shelf Button:
import AAikman_AimConstraintAll as aaaca
reload(aaaca)
aaaca.main()

Marking Menu Script:
python("import AAikman_AimConstraintAll as aaaca; reload(aaaca); aaaca.main();")

'''
import maya.cmds as cmds
from AAikman_Utils import snapTo

def main():
	sel = cmds.ls(sl=True)
	oSel = sel
	parObj = sel[-1]
	sel.pop()

	for i in sel:
	    cmds.select(parObj, r=True)
	    cmds.aimConstraint(parObj, i, mo=True)

	cmds.select(oSel, r=True)