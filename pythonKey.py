import os, sys
import datetime
import cv2
from pynput import mouse 
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener, KeyCode

def on_move(x, y):
	print('Pointer moved to {0}'.format(
		(x, y)))
	return False

def on_click(x, y, button, pressed):
	print('{0} at {1}'.format(
		'Pressed' if pressed else 'Released',
		(x, y)))
	return False
	#if not pressed:
		# Stop listener
		#return False

def on_scroll(x, y, dx, dy):
	print('Scrolled {0} at {1}'.format(
		'down' if dy < 0 else 'up',
		(x, y)))
	return False

def on_press(key):
	print('{0} pressed'.format(
		key))
	return False

def on_release(key):
	print('{0} release'.format(
		key))
	return False
	#if key == Key.esc:
		# Stop listener
		#return False

def main():
	x = datetime.datetime.now()

	with open("C:\\Ruben\\NOS\\powershell\\lock-PC\\doNotDeleteMe.txt",'w') as f:
		f.write("0")
		f.close()
	# Collect events until released
	with Listener(
			on_press=on_press,
			on_release=on_release,
			on_move=on_move,
			on_click=on_click,
			on_scroll=on_scroll) as listenerK:
		listenerK.join()

	# ...or, in a non-blocking fashion:
	listener = Listener(
		on_press=on_press,
		on_release=on_release,
		on_move=on_move,
		on_click=on_click,
		on_scroll=on_scroll)
	listener.start()
	
	imgName = "C:\\Ruben\\NOS\\powershell\\lock-PC\\img\\" + x.strftime("%f") + ".png"

	with open("C:\\Ruben\\NOS\\powershell\\lock-PC\\doNotDeleteMe.txt",'w') as f:
		f.write("1")
		f.close()
	
	camera = cv2.VideoCapture(0)
	for i in range(10):
		return_value, image = camera.read()
		cv2.imwrite(imgName, image)
	
main()