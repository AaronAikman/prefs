import maya.cmds as cmds
sel = cmds.ls(sl=True)

children = []
for itm in sel:
    try:
        cmds.select(itm, r=True)
        children.append(cmds.listRelatives(c=True)[0])
        
cmds.select(children, r=True)