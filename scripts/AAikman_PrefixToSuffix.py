'''
Author:
Aaron Aikman

Date of Creation:
2/5/2018

Installation:
Put in scripts folder
Enter 'rehash' in the mel command line
Put the Shelf Button script into a python button

Shelf Button:
import AAikman_PrefixToSuffix as aaPrefToSuf
reload(aaPrefToSuf)
aaPrefToSuf.main()

Marking Menu Script:
python("import AAikman_PrefToSuf as aaPrefToSuf; reload(aaPrefToSuf); aaPrefToSuf.main();")

'''
import pymel.core as pm

def main():
    for i in pm.selected():
        nameToCheck = str(i)
        if 'L_' in nameToCheck:
            newName = nameToCheck.replace('L_', '') + '_L'
            i.rename(newName)
            print 'Renamed {} to {}'.format(nameToCheck, newName)
        elif 'R_' in nameToCheck:
            newName = nameToCheck.replace('R_', '') + '_R'
            i.rename(newName)
            print 'Renamed {} to {}'.format(nameToCheck, newName)
