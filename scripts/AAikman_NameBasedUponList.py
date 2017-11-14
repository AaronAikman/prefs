import maya.cmds as cmds

sel = cmds.ls(sl=True)
startIter = 0

nameList = ('Brow',
	'Jaw',
	'Mouth',
	'Twist',
	'Bend',
	'Eyelid',
	'PhonemeVowel',
	'PhonemeCons',
	'PhonemeOther')

suffixToUse = '_ctrl'

for i in sel:
	if nameList[startIter]:
		nameToRename = '{}{}'.format(nameList[startIter], suffixToUse)
		cmds.rename(i, nameToRename)
		startIter += 1