from functions import * 
import datetime

def main():
	x = datetime.datetime.now()
	
	pathToScript = sys.argv[1]

	#Get the config variables defined by the user
	supportFile = str(pathToScript) + setConfigVars("doNotDelete", pathToScript)
	imgFolder = str(pathToScript) + setConfigVars("img", pathToScript)
	imgName = imgFolder + x.strftime("%f") + ".png"

	print(supportFile)
	print(imgFolder)
	print(imgName)
	#Reset the value in the file, to ensure it only locks after the keyboard or mouse usage
	writeInFile(supportFile,"0")

	# Starting Mouse Listener
	listener = mouse.Listener(
		on_press=on_press,
		on_release=on_release,
		on_move=on_move,
		on_click=on_click,
		on_scroll=on_scroll)
	listener.start()

	# Starting Keyboard Listener
	listener = keyboard.Listener(
		on_press=on_press,
		on_release=on_release)
	listener.start()
	
	writeInFile(supportFile,"1")
	
	camera = cv2.VideoCapture(0)
	for i in range(10):
		return_value, image = camera.read()
		cv2.imwrite(imgName, image)
	
main()