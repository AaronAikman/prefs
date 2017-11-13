import maya.cmds as cmds

sel = cmds.ls(sl=True)
toParentTo = ''

for i in sel:
    cmds.select(i, r=True)
    if toParentTo:
        cmds.parent(i, toParentTo)
    toParentTo = i