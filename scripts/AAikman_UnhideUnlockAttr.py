'''
Author:
Aaron Aikman

Date of Creation:
12/08/2017

Installation:
Put in scripts folder

Shelf Button:
import AAikman_UnhideUnlockAttr as aaUnAttr
reload(aaUnAttr)
aaUnAttr.main()

Marking Menu Script
python( "import AAikman_UnhideUnlockAttr as aaUnAttr; reload(aaUnAttr); aaUnAttr.main(0);" )
python( "import AAikman_UnhideUnlockAttr as aaUnAttr; reload(aaUnAttr); aaUnAttr.main(1);" )
'''


import pymel.core as pm
basicAttr = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']

def main(modeType=0):
    '''
    0 = Unlock
    1 = Lock
    '''
    sel = pm.selected()
    if modeType == 0:
        lockVal = False
        keyVal = True
    else:
        lockVal = True
        keyVal = False

    for obj in sel:
        print obj
        for at in basicAttr:
            atToMod = '{}.{}'.format(obj,at)
            pm.setAttr(atToMod, lock=lockVal)
            pm.setAttr(atToMod, keyable=keyVal)
