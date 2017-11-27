'''
Author:
Aaron Aikman

Date of Creation:
11/21/2017

Installation:
Put in scripts folder

Shelf Button:
import AAikman_CircleAtSel as aacas
reload(aacas)
aacas.main()

Marking Menu Script
python( "import AAikman_CircleAtSel as aacas; reload(aacas); aacas.main();" ) 
'''

import maya.cmds as cmds
import maya.mel as mel

ctrlSize = 30

def main():
    sel = cmds.ls(sl=True)
    for i in sel:
        cmds.select(i, r=True)
        loc = cmds.xform(q=True, t=True, ws=True)
        
        if i.endswith('_jnt'):
            ctrlName = i[:-4]
        else:
            ctrlName = i

        curCtrlName = '{}_ctrl'.format(ctrlName)

        cmds.circle(n=curCtrlName)
        cmds.move(loc[0], loc[1], loc[2])
        cmds.scale(ctrlSize, ctrlSize, ctrlSize)
        mel.eval("performFreezeTransformations(0)")
        cmds.delete(ch=True)
        cmds.parentConstraint(curCtrlName, i, mo=True)
        