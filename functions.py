import os, sys
import cv2
from pynput import mouse 
from pynput.mouse import Button, Listener, Controller
from pynput import keyboard
from pynput.keyboard import Key, Listener, KeyCode

def setConfigVars(key, pathToScript):
	configFile = str(pathToScript) + '\\vars.config'
	with open(configFile) as fi:
		lines = fi.readlines()
		for line in lines:
			line = line.replace('\n','')
			content = line.split(",,")
			if content[0] == key:
				return content [1]
		return null

def on_move(x, y):
	print('Pointer moved to {0}'.format(
		(x, y)))
	return False

def on_click(x, y, button, pressed):
	print('{0} at {1}'.format(
		'Pressed' if pressed else 'Released',
		(x, y)))
	return False

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

def writeInFile(FilePath,text):
	with open(FilePath,'w') as f:
		f.write(text)
		f.close()