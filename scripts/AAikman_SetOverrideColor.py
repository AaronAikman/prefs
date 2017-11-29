'''
Author:
Aaron Aikman

Date of Creation:
11/28/2017

Installation:
Put in scripts folder

Shelf Button:
import AAikman_SetOverrideColor as aaSetColor
reload(aaSetColor)
aaSetColor.main()

Marking Menu Script
python( "import AAikman_SetOverrideColor as aaSetColor; reload(aaSetColor); aaSetColor.main();" ) 
python( "import AAikman_SetOverrideColor as aaSetColor; reload(aaSetColor); aaSetColor.main('red');" ) 
python( "import AAikman_SetOverrideColor as aaSetColor; reload(aaSetColor); aaSetColor.main('yellow');" ) 
python( "import AAikman_SetOverrideColor as aaSetColor; reload(aaSetColor); aaSetColor.main('cyan');" ) 
python( "import AAikman_SetOverrideColor as aaSetColor; reload(aaSetColor); aaSetColor.main('green');" ) 
python( "import AAikman_SetOverrideColor as aaSetColor; reload(aaSetColor); aaSetColor.main('pink');" ) 
python( "import AAikman_SetOverrideColor as aaSetColor; reload(aaSetColor); aaSetColor.main('black');" ) 
python( "import AAikman_SetOverrideColor as aaSetColor; reload(aaSetColor); aaSetColor.main('white');" ) 
python( "import AAikman_SetOverrideColor as aaSetColor; reload(aaSetColor); aaSetColor.main('random');" ) 
'''

import maya.cmds as cmds
from random import randint


def main(clr = 'blue'):
    sel = cmds.ls(sl=True)
    clr = clr.lower()
    for i in sel:
        # shapeName = '{}Shape'.format(i)
        # if cmds.objExists(shapeName):
        #     changeCurveColor(shapeName, clr)
        # else:
        children = cmds.listRelatives(c=True, pa=True)
        for child in children:
            if cmds.objectType(child) == 'nurbsCurve':
                print child
                changeCurveColor(child, clr)


def changeCurveColor(obj, clr):
    if cmds.objExists(obj):
        # clr = str(clr)
        cmds.setAttr('{}.overrideEnabled'.format(obj), True)
        if clr == 'blue':
            cmds.setAttr('{}.overrideColor'.format(obj), 6)
        elif clr == 'red':
            cmds.setAttr('{}.overrideColor'.format(obj), 13)
        elif clr == 'yellow':
            cmds.setAttr('{}.overrideColor'.format(obj), 17)
        elif clr == 'cyan':
            cmds.setAttr('{}.overrideColor'.format(obj), 18)
        elif clr == 'green':
            cmds.setAttr('{}.overrideColor'.format(obj), 14)
        elif clr == 'pink':
            cmds.setAttr('{}.overrideColor'.format(obj), 9)
        elif clr == 'black':
            cmds.setAttr('{}.overrideColor'.format(obj), 1)
        elif clr == 'white':
            cmds.setAttr('{}.overrideColor'.format(obj), 16)
        else:
            cmds.setAttr('{}.overrideColor'.format(obj), randint(0, 25))