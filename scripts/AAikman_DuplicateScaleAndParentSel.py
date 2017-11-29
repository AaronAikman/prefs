'''
Author:
Aaron Aikman

Date of Creation:
11/21/2017

Installation:
Put in scripts folder

Shelf Button:
import AAikman_DuplicateScaleAndParentSel as aaDupScaleReparent
reload(aaDupScaleReparent)
aaDupScaleReparent.main()

Marking Menu Script
python( "import AAikman_DuplicateScaleAndParentSel as aaDupScaleReparent; reload(aaDupScaleReparent); aaDupScaleReparent.main();" ) 
'''

import maya.cmds as cmds
import maya.mel as mel

def main():
    newScale = 1.5


    sel = cmds.ls(sl=True)

    for i in sel:
        cmds.select(i, r=True)
        parName = '{}_parent'.format(i)
        cmds.duplicate(n=parName)
        cmds.scale(newScale, newScale, newScale)
        cmds.select(parName, r=True)
        mel.eval("performFreezeTransformations(0)")
        cmds.parent(i, parName)
        