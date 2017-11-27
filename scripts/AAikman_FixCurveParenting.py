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
import AAikman_FixCurveParenting as aafcp
reload(aafcp)
aafcp.main()

Marking Menu Script:
python("import AAikman_FixCurveParenting as aafcp; reload(aafcp); aafcp.main();")

'''

import maya.cmds as cmds

def main():
    sel = cmds.ls(sl=True)
    frozeTransAlready = 1

    for i in sel:
        cmds.select(i, r=True)
        cmds.select(hi=True)
        if not frozeTransAlready:
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
            frozeTransAlready = 1
        currentNodes = cmds.ls(sl=True)
        for j in currentNodes:
            if cmds.objectType(j, isType='nurbsCurve'):
                try:
                    cmds.parent(j, i, s=True, r=True)
                except:
                    print 'Could not reparent {}'.format(j)
        cmds.select(i, r=True)
        cmds.select(hi=True)
        nodesToPotentiallyDelete = cmds.ls(sl=True)
        nodesToPotentiallyDelete.pop(0)

        for k in nodesToPotentiallyDelete:
            if cmds.objExists(k):
                if cmds.objectType(k, isType='transform'):
                    cmds.delete(k)
