from functions import * 
from scout import * 
import datetime

def main():
	x = datetime.datetime.now()
	catchValue = "0"

	#pathToScript = sys.argv[2]
	pathToScript = "C:\\Ruben\\GitHub\\WindowsLock"

	#Get the config variables defined by the user
	supportFile = str(pathToScript) + setConfigVars("doNotDelete", pathToScript)
	imgFolder = str(pathToScript) + setConfigVars("img", pathToScript)
	password = setConfigVars("password", pathToScript)
	imgName = imgFolder + x.strftime("%f") + ".png"

	#Reset the value in the file, to ensure it only locks after the keyboard or mouse usage
	writeInFile(supportFile,catchValue)

	s = scout(password)
	s.start()

	writeInFile(supportFile,s.signal)
	
	camera = cv2.VideoCapture(0)
	for i in range(10):
		return_value, image = camera.read()
		cv2.imwrite(imgName, image)
	
main()