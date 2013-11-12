### Wii Nunchuk to Maya proof of concept
### http://zoomy.net/2010/04/11/wii-nunchuk-to-maya/
###
sys.path.append( "C:\Program Files\Common Files\Python\Python25\Lib\site-packages\win32")
sys.path.append( "C:\Program Files\Common Files\Python\Python25\Lib\site-packages\win32\lib")
import time, sys, serial, win32file, win32con, re
import maya.cmds as cmds
import maya.mel as mel

try: ser
except: 1
else: ser.close()

# open serial connection - adjust settings for your input device
ser = serial.Serial(
  port='COM3',
  baudrate=19200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS
)

sphere1 = polySphere(n="sphere1")[0]
cmds.setAttr(sphere1+".scaleY", 2)
flare=nonLinear(type='flare')[0]
cmds.setAttr(flare+".startFlareX",1.5)
cmds.setAttr(flare+".startFlareZ",1.5)
cmds.setAttr(flare+"Handle.visibility",0)

# progress bar, enabling "Esc"
gMainProgressBar = mel.eval('$tmp = $gMainProgressBar');
cmds.progressBar( gMainProgressBar,
        edit=True,
        beginProgress=True,
        isInterruptable=True,
        status='Reading serial data...' )
        
while 1:
  data = ser.readline()
  data = data.split(';')
  data[1] = data[1][:-2]
  print data

  cmds.setAttr(sphere1+".rotateZ", (float(data[0])*-1)-45)
  cmds.setAttr(sphere1+".rotateX", float(data[1])+90)
  refresh() # update the viewscreen

  if cmds.progressBar(gMainProgressBar, query=True, isCancelled=True ) :
    delete(whichObj)
    break

ser.close()
cmds.progressBar(gMainProgressBar, edit=True, endProgress=True)

###