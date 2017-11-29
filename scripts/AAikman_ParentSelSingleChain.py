'''
Author:
Aaron Aikman

Date of Creation:
11/21/2017

Installation:
Put in scripts folder

Shelf Button:
import AAikman_ParentSelSingleChain as aaSingleHeir
reload(aaSingleHeir)
aaSingleHeir.main()

Marking Menu Script
python( "import AAikman_ParentSelSingleChain as aaSingleHeir; reload(aaSingleHeir); aaSingleHeir.main();" ) 
'''

import maya.cmds as cmds

def main():
    sel = cmds.ls(sl=True)
    toParentTo = ''

    for i in sel:
        cmds.select(i, r=True)
        if toParentTo:
            cmds.parent(i, toParentTo)
        toParentTo = i