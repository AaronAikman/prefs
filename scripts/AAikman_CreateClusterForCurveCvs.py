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
import AAikman_CreateClusterForCurveCvs as aaClusterCurve
reload(aaClusterCurve)
aaClusterCurve.main()

Marking Menu Script:
python("import AAikman_CreateClusterForCurveCvs as aaClusterCurve; reload(aaClusterCurve); aaClusterCurve.main();")

'''

import maya.cmds as cmds

def main():
    sel = cmds.ls(sl=True)
    for i in sel:
        cmds.select(i, r=True)
        shapes = cmds.listRelatives(c=True, pa=True)
        for shape in shapes:
            if cmds.objectType(shape) == 'nurbsCurve':
                numCVs = cmds.getAttr('{}.spans'.format(shape)) + cmds.getAttr('{}.degree'.format(shape)) # - 1
                numCVs = cmds.getAttr('{}.spans'.format(shape)) # + cmds.getAttr('{}.degree'.format(shape)) # - 1
                print numCVs
                for n in range(numCVs):
                    try:
                        cmds.select("{}.cv[{}]".format(i, n))
                        cmds.cluster()
                    except:
                        print 'Failed on {}.cv[{}]'.format(i, n)