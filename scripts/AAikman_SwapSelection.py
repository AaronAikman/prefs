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
import AAikman_SwapSelection as aaSwapSel
reload(aaSwapSel)
aaSwapSel.main()

Marking Menu Script:
python("import AAikman_SwapSelection as aaSwapSel; reload(aaSwapSel); aaSwapSel.main();")

'''

import maya.cmds as cmds

def main():
    ind = 0
    sel = cmds.ls(sl=True)
    cmds.select(sel[-1], r=True)
    sel.pop()
    sel = sel[::-1]
    for i in sel:
        cmds.select(i, add=True)
