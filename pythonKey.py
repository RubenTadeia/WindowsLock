from functions import * 
import datetime

def main():
	x = datetime.datetime.now()
	
	#Get the config variables defined by the user
	supportFile = setConfigVars("doNotDelete")
	imgFolder = setConfigVars("img")
	imgName = imgFolder + x.strftime("%f") + ".png"

	#Set
	writeInFile(supportFile,"0")

	# Collect events until released
	with Listener(
			on_press=on_press,
			on_release=on_release,
			on_move=on_move,
			on_click=on_click,
			on_scroll=on_scroll) as listenerK:
		listenerK.join()

	# ...or, in a non-blocking fashion:
	#listener = Listener(
	#	on_press=on_press,
	#	on_release=on_release,
	#	on_move=on_move,
	#	on_click=on_click,
	#	on_scroll=on_scroll)
	#listener.start()
	
	writeInFile(supportFile,"1")
	
	camera = cv2.VideoCapture(0)
	for i in range(10):
		return_value, image = camera.read()
		cv2.imwrite(imgName, image)
	
main()