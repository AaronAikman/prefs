'''
Author:
Aaron Aikman

Owner:
Blind Squirrel Entertainment

Date of Creation:
11/08/2017

Installation:
Put in scripts folder

Shelf Button:
import AAikman_PyToMelMM as aaptm
reload(aaptm)

Usage:
Select the Root joints of components you want to export
These root joints should not have any parents
Do not select anything but the root joints
Choose destination and naming options
Click the run button
Note that this process will overwrite files

Process:
The script will bake the keys onto the joints and export them
with the correct settings to the correct location

'''
import maya.cmds as cmds


startDir = 'D:/Almond/Main/Art/Source/Animation'
startChar = 'Sumo'
startAnim = 'TemplateAnim'
bakeInScene = False

scriptName = 'aaptm'
hts = 100
wts = 250

# scrollField -wordWrap true -text "Multilines!" -editable true;

def main():
    WinName = 'PyToMelWindow'

    if (cmds.window(WinName, exists=True)):
        cmds.deleteUI(WinName)
    cmds.window( WinName, title='Convert Python to Mel')
        
    cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'left', 0), width=wts, h=hts )

    # cmds.text( label='Animation Name' )
    global textToConvert
    # textToConvert = cmds.textField(text=startAnim)
    textToConvert = cmds.scrollField( wordWrap=True, text="Paste Python code here.\nThen click Convert.", editable=True)
    # cmds.separator()

    # cmds.separator()
    cmds.button(label='Convert', command='{}.convertText()'.format(scriptName))
    # cmds.separator()
    cmds.window(WinName, e=True, width=wts, h=hts)
    cmds.showWindow()


def convertText():
    pyText = cmds.scrollField(textToConvert, q=True, tx=True)
    convertedPy = 'python("{};")'.format('; '.join([s.strip() for s in pyText.splitlines()]))
    cmds.scrollField(textToConvert, edit=True, tx=convertedPy)

main()