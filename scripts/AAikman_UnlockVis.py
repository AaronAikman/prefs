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

Marking Menu Script:
python("import AAikman_UnlockVis as aauv; reload(aauv); aauv.main();")
python("import AAikman_UnlockVis as aauv; reload(aauv); aauv.main(0);")

'''

import maya.cmds as cmds

sel = cmds.ls(sl=True)

def main(mode=1):
    for i in sel:
        cmds.select(i, r=True)
        # pivLocFull = cmds.xform(q=True, piv=True, a=True)
        # print pivLoc
        visName ='{}.visibility'.format(i)
        if mode:
            cmds.setAttr(visName, l=False)
            cmds.setAttr(visName, k=True)
        else:
            cmds.setAttr(visName, l=True)
            cmds.setAttr(visName, k=False)
    cmds.select(sel, r=True)

# main()