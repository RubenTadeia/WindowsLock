import os, sys
import cv2
from pynput import mouse 
from pynput import keyboard

class scout:

	def __init__(self,password):
		self.Triggered = False
		self.pwd = password
		self.signal = "0"

	def on_move(self, x, y):
		#print('Pointer moved to {0}'.format(
		#	(x, y)))
		self.Triggered = True
		self.signal = "1"
		return False

	def on_click(self, x, y, button, pressed):
		#print('{0} at {1}'.format(
		#	'Pressed' if pressed else 'Released',
		#	(x, y)))
		self.Triggered = True
		self.signal = "1"
		return False

	def on_scroll(self, x, y, dx, dy):
		#print('Scrolled {0} at {1}'.format(
		#	'down' if dy < 0 else 'up',
		#	(x, y)))
		self.Triggered = True
		self.signal = "1"
		return False

	def on_press(self, key):
		#print('{0} pressed'.format(
		#	key))
		self.Triggered = True
		return False

	def on_release(self, key):
		#print('{0} release'.format(
		#	key))
		self.Triggered = True
		return False

	def start(self):
		# Starting Mouse Listener
		mlistener = mouse.Listener(
			on_move=self.on_move,
			on_click=self.on_click,
			on_scroll=self.on_scroll)
		mlistener.start()
		# Starting Keyboard Listener
		klistener = keyboard.Listener(
			on_press=self.on_press,
			on_release=self.on_release)
		klistener.start()

		while self.Triggered == False:
			# wait
			pass