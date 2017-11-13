import maya.cmds as cmds
for itm in cmds.ls(sl=True):
    cmds.addAttr( longName='AimStrength', attributeType='float', k=True, minValue=0, maxValue=1, defaultValue=1)