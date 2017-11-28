'''
Author:
Aaron Aikman

Date of Creation:
11/21/2017

Installation:
Put in scripts folder
Enter 'rehash' in the mel command line
Put the Shelf Button script into a python button

Shelf Button:
import AAikman_AddAttrToSel as aaAddAttrs
reload(aaAddAttrs)
aaAddAttrs.main()

Marking Menu Script:
python("import AAikman_AddAttrToSel as aaAddAttrs; reload(aaAddAttrs); aaAddAttrs.main();")

'''

import maya.cmds as cmds

def main():
    sel = cmds.ls(sl=True)
    for itm in sel:
        cmds.select(itm, r=True)
        # cmds.addAttr( longName='ArmorUp', attributeType='float', k=True, minValue=0, maxValue=10, defaultValue=0)
        # cmds.addAttr( longName='ArmorUp_SideL', attributeType='float', k=True, minValue=0, maxValue=1, defaultValue=0)
        # cmds.addAttr( longName='ArmorUp_SideR', attributeType='float', k=True, minValue=0, maxValue=1, defaultValue=0)
        # cmds.addAttr( longName='ArmorUp_Visor3', attributeType='float', k=True, minValue=0, maxValue=1, defaultValue=0)
        # cmds.addAttr( longName='ArmorUp_Visor2', attributeType='float', k=True, minValue=0, maxValue=1, defaultValue=0)
        # cmds.addAttr( longName='ArmorUp_Visor1', attributeType='float', k=True, minValue=0, maxValue=1, defaultValue=0)
        # cmds.addAttr( longName='ArmorUp_JawUpper', attributeType='float', k=True, minValue=0, maxValue=1, defaultValue=0)
        # cmds.addAttr( longName='ArmorUp_JawLower', attributeType='float', k=True, minValue=0, maxValue=1, defaultValue=0)
        cmds.addAttr( longName='ControlVis_Armor', attributeType='float', k=True, minValue=0, maxValue=1, defaultValue=1)
        cmds.addAttr( longName='ControlVis_Propulsion', attributeType='float', k=True, minValue=0, maxValue=1, defaultValue=1)
        cmds.addAttr( longName='ControlVis_Grapple', attributeType='float', k=True, minValue=0, maxValue=1, defaultValue=1)
