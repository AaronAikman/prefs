offsetAmt = 1
for i in range(2, 93):
	jointNum = i
	offsetNum = offsetAmt
	print 'Chain_jnt_{jn}.sx = clamp(0, 1, (Hand_L_ctrl.Chain * $ChainMod) - {on});\nChain_jnt_{jn}.sy = clamp(0, 1, (Hand_L_ctrl.Chain * $ChainMod) - {on});\nChain_jnt_{jn}.sz = clamp(0, 1, (Hand_L_ctrl.Chain * $ChainMod) - {on});\n\n'.format(jn=jointNum, on=offsetNum)
	offsetAmt += 1