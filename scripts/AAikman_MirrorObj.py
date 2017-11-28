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
import AAikman_MirrorObj as aaMirrorObj
reload(aaMirrorObj)
aaMirrorObj.main()

Marking Menu Script:
python("import AAikman_MirrorObj as aaMirrorObj; reload(aaMirrorObj); aaMirrorObj.main();")

'''
import maya.cmds as cmds

def main(dir = [-1,1,1]):
    
    t = 'TempGroup'
    sel = cmds.ls(sl=True)
    dupedObj = []
    l = '_L'
    r = '_R'
    for i in sel:
        oI = i
        if l in i:
            dupName = i.replace(l, r)
            if cmds.objExists(dupName):
                cmds.delete(dupName)
            cmds.duplicate(n=dupName)
        elif r in i:
            dupName = i.replace(r, l)
            if cmds.objExists(dupName):
                cmds.delete(dupName)
            cmds.duplicate(n=dupName)
        else:
            renamedObj = False
            iterStart = 1
            while not renamedObj:
                try:
                    dupName = '{}_{}'.format(i, iterStart)
                    cmds.duplicate(n=dupName)
                    renamedObj = True
                except:
                    iterStart += 1

        dupedObj.append(dupName)


    cmds.select(dupedObj)
    cmds.group(n=t)
    cmds.select(t)
    cmds.xform(piv=[0,0,0])
    cmds.xform(s = dir)
    cmds.makeIdentity(t, apply=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.select(dupedObj)
    cmds.parent(w=True)
    cmds.delete(t)
    cmds.select(dupedObj)


    for j in dupedObj:
        dupChildren = cmds.listRelatives(j, ad=True, pa=True)
        if len(dupChildren) > 0:
            for k in dupChildren:
                shortName = k.split('|')[-1]
                if l in k:
                    cmds.rename(k, shortName.replace(l, r))
                elif r in k:
                    cmds.rename(k, shortName.replace(r, l))
                    # cmds.rename(k, k.replace(r, l))

