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
aaaca.main(0, True)

Marking Menu Script:
python("import AAikman_AimConstraintAll as aaaca; reload(aaaca); aaaca.main(0, True);")

'''
import maya.cmds as cmds

def main(useObjUp=0, maintOff=True):
    sel = cmds.ls(sl=True)
    oSel = sel
    parObj = sel[0]
    sel.pop(0)

    if useObjUp:
        upObj = sel[-1]
        sel.pop()

    for i in sel:
        cmds.select(parObj, r=True)
        if useObjUp:
            cmds.aimConstraint(parObj, i, mo=maintOff, worldUpType="object", worldUpObject=upObj)
        else:
            cmds.aimConstraint(parObj, i, mo=maintOff)

    cmds.select(oSel, r=True)