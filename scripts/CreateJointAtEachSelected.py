import maya.cmds as cmds

sel = cmds.ls(sl=True)
jointPrev = ''
for link in sel:
    cmds.select(link, r=True)
    loc = cmds.xform(q=True, piv=True)
    cmds.select(cl=True)
    if jointPrev:
        cmds.select(jointPrev)
    jointPrev = cmds.joint()
    cmds.move(loc[0], loc[1], loc[2])