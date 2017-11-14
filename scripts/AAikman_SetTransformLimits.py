import maya.cmds as cmds

sel = cmds.ls(sl=True)
whichAxis = [1, 0, 1]
limitValue = 20
setMinToZero = 0

for i in sel:
	cmds.transformLimits(i, tx=(-(limitValue * whichAxis[0] * (1 - setMinToZero)), (limitValue * whichAxis[0])),
							ty=(-(limitValue * whichAxis[1] * (1 - setMinToZero)), (limitValue * whichAxis[1])),
							tz=(-(limitValue * whichAxis[2] * (1 - setMinToZero)), (limitValue * whichAxis[2])),
							etx=[1,1],
							ety=[1,1],
							etz=[1,1])
	print 'Processed ' + i

