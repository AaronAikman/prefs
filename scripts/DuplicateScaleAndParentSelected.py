import maya.cmds as cmds
import maya.mel as mel

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
    