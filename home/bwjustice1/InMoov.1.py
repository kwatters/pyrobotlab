inMoov = Runtime.createAndStart("inMoov", "InMoov")
rightSerialPort = "COM8"
cameraIndex = 1
 
# attach an arduino to InMoov
# possible board types include uno atmega168 atmega328p atmega2560 atmega1280 atmega32u4
# the MRLComm.ino sketch must be loaded into the Arduino for MyRobotLab control !
# set COM number according to the com of your Arduino board
inMoov.attachArduino("right","uno", rightSerialPort)
 

# attach the right hand
inMoov.attachHand("right")

# system check
inMoov.systemCheck()

# listen for these key words
# to get voice to work - you must be attached to the internet for
# at least the first time
ear = inMoov.getEar()
ear.addCommand("rest", inMoov.getName(), "rest")
ear.addCommand("open hand", inMoov.getName(), "handOpen", "right")
ear.addCommand("close hand", inMoov.getName(), "handClose", "right")
ear.addCommand("capture gesture", inMoov.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")
ear.addComfirmations("yes","correct","yeah","ya") 
ear.addNegations("no","wrong","nope","nah")
 
ear.startListening()
