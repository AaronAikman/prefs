for i in cmds.ls(sl=True): cmds.select(i, r=True); print cmds.xform(q=True, t=True); print cmds.xform(q=True, ro=True)