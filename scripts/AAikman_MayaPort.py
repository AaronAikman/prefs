'''
Author:
Aaron Aikman

Date of Creation:
12/08/2017

Installation:
Put in scripts folder

Shelf Button:
import AAikman_MayaPort as aaMayaPort
reload(aaMayaPort)
aaMayaPort.main()

Marking Menu Script
python( "import AAikman_MayaPort as aaMayaPort; reload(aaMayaPort); aaMayaPort.main(0);" )
python( "import AAikman_MayaPort as aaMayaPort; reload(aaMayaPort); aaMayaPort.main(1);" )
'''

import maya.cmds as cmds
def main(openNew = 1):
    # Open new ports
    try:
        # cmds.commandPort(name=":7001", close=True)
        cmds.commandPort(name=":7002", close=True)
    except:
        if openNew:
        # cmds.commandPort(name=":7001", sourceType="mel", echoOutput=True)
            cmds.commandPort(name=":7002", sourceType="python", echoOutput=True)
