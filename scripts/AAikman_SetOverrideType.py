'''
Author:
Aaron Aikman

Date of Creation:
12/08/2017

Installation:
Put in scripts folder

Shelf Button:
import AAikman_SetOverrideType as aaSetOverrideType
reload(aaSetOverrideType)
aaSetOverrideType.main()

Marking Menu Script
python( "import AAikman_SetOverrideType as aaSetOverrideType; reload(aaSetOverrideType); aaSetOverrideType.main(0);" )
python( "import AAikman_SetOverrideType as aaSetOverrideType; reload(aaSetOverrideType); aaSetOverrideType.main(1);" )
python( "import AAikman_SetOverrideType as aaSetOverrideType; reload(aaSetOverrideType); aaSetOverrideType.main(2);" )
'''

import maya.cmds as cmds


def main(modeType = 2):
    '''
    0 = Normal
    1 = Template
    2 = Reference
    '''

    sel = cmds.ls(sl=True)
    for obj in sel:
        cmds.setAttr('{}.overrideEnabled'.format(obj), True)
        cmds.setAttr('{}.overrideDisplayType'.format(obj), modeType)