
import maya.cmds as cmds

sel = cmds.ls(sl=True)
times = 100
for i in sel:
	cmds.duplicate()
	cmds.move(10,50,0,r=True)
	cmds.rotate(45,45,0, r=True)
	for j in range(times):
		cmds.duplicate(st=True)
		# cmds.move(10,10,0,r=True)
		# cmds.rotate(0,45,0, r=True)
