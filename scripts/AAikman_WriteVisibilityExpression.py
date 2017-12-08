offsetAmt = 14
for i in range(3, 18):
	jointNum = offsetAmt + 3
	offsetNum = offsetAmt
	# print 'Chain_jnt_{jn}.sx = clamp(0, 1, (Hand_L_ctrl.Chain * $ChainMod) - {on});\nChain_jnt_{jn}.sy = clamp(0, 1, (Hand_L_ctrl.Chain * $ChainMod) - {on});\nChain_jnt_{jn}.sz = clamp(0, 1, (Hand_L_ctrl.Chain * $ChainMod) - {on});\n\n'.format(jn=jointNum, on=offsetNum)
	print 'Chain_{jn}_ctrl_parent.visibility = clamp(0, 1, (Hand_L_ctrl.Chain * $ChainVisMod) - {on});\n\n'.format(jn=jointNum, on=offsetNum)
	offsetAmt -= 1