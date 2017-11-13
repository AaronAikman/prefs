import maya.cmds as cmds
import maya.mel as mel

# Vars
ctrlName = 'Chain'
ctrlSize = 30

# Leave Alone
ctrlStartIter = 1

sel = cmds.ls(sl=True)
for i in sel:
    cmds.select(i, r=True)
    loc = cmds.xform(q=True, piv=True)
    curCtrlName = '{}_ctrl_{}'.format(ctrlName, ctrlStartIter)
    ctrlStartIter += 1
    cmds.circle(n=curCtrlName)
    cmds.move(loc[0], loc[1], loc[2])
    cmds.scale(ctrlSize, ctrlSize, ctrlSize)
    mel.eval("performFreezeTransformations(0)")
    cmds.parentConstraint(curCtrlName, i)
    