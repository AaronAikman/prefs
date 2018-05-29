'''
Author:
Aaron Aikman

Date of Creation:
01/21/2018

Installation:
Put in scripts folder

Shelf Button:
import AAikman_FilterSelectionToConstraints as aafstc
reload(aafstc)
aafstc.main()

Marking Menu Script
python( "import AAikman_FilterSelectionToConstraints as aafstc; reload(aafstc); aafstc.main();" ) 
'''

import pymel.core as pm

def main():
    sel = pm.selected()
    pm.select(cl=True)
    for i in sel:
        if i.name().endswith('Constraint'):
            pm.select(i, add=True)
        elif i.name()[-11:-1] == 'Constraint':
            pm.select(i, add=True)
