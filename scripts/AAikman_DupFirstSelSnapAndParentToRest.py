# DuplicateFirstSelectedSnapAndParentToRest

import maya.cmds as cmds
from AAikman_Utils import snapTo

sel = cmds.ls(sl=True)
oSel = sel
toDup = sel[0]
sel.pop(0)
iterStart = 1

for i in sel:
    dupName = '{}_{}'.format(toDup, iterStart)
    iterStart += 1
    cmds.select(toDup, r=True)
    cmds.duplicate(n= dupName)
    snapTo(i, dupName)
    cmds.parent(dupName, i)


cmds.select(oSel, r=True)