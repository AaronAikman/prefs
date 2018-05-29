'''
Author:
Aaron Aikman

Date of Creation:
2/20/2018

Installation:
Put in scripts folder
Enter 'rehash' in the mel command line
Put the Shelf Button script into a python button

Shelf Button:
import AAikman_MakeArt as aaMakeArt
reload(aaMakeArt)
aaMakeArt.main()

Marking Menu Script:
python("import AAikman_MakeArt as aaMakeArt; reload(aaMakeArt); aaMakeArt.main();")

'''
import pymel.core as pm
dirsCube = [[1,1,1],
        [1,1,-1],
        [1,-1,-1],
        [-1,-1,-1],
        [-1,-1,1],
        [-1,1,1],
        [1,-1,1],
        [-1,1,-1]]

dirs = [[1,1,1],
        [1,1,-1],
        [1,-1,-1],
        [-1,-1,-1],
        [-1,-1,1],
        [-1,1,1],
        [1,-1,1],
        [1.5,0,0],
        [-1.5,0,0],
        [0,1.5,0],
        [0,-1.5,0],
        [0,0,1.5],
        [0,0,-1.5],
        [-1,1,-1]]

def main(arms = 3, iters = 10, mag = 5, doCube = False):
    for i in pm.selected():
        for b in range(arms):
            dirsToUse = []
            if doCube:
                dirsToUse = dirsCube
            else:
                dirsToUse = dirs

            for a in dirsToUse:
                pm.select(i)
                for j in range(iters + 1):
                    k = pm.duplicate()
                    trans = [x * mag for x in a]
                    pm.move( trans, r=True)
                    pm.rotate( '12deg', 0, 0, r=True)