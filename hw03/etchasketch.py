#!/usr/bin/env python3

import sys
import time
import Adafruit_BBIO.GPIO as GPIO
import smbus
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2

bus = smbus.SMBus(1)	#Use i2c bus 1
matrix = 0x70		#Use address

hEncoder = RotaryEncoder(eQEP2)
vEncoder = RotaryEncoder(eQEP1)
hEncoder.setAbsolute()
vEncoder.setAbsolute()
hEncoder.enable()
vEncoder.enable()
hPos = hEncoder.position
vPos = vEncoder.position

but0 = "P9_14"
but1 = "P9_13"
but2 = "P9_12"
but3 = "P9_11"
GPIO.setup(but0, GPIO.IN)
GPIO.setup(but1, GPIO.IN)
GPIO.setup(but2, GPIO.IN)
GPIO.setup(but3, GPIO.IN)

gridSize = 8
lines = 0
cols = 0

coordx = 0
coordy = 7
screen = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def refreshScreen():
	global coordy
	global coordx
	screen[2*coordx] |= 1<<coordy
	bus.write_i2c_block_data(matrix, 0, screen)

def detectedInput(channel):
	global coordy
	global coordx
	global screen
	if channel == but0:
		#newX = (coordx+1)%8
		screen = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	elif channel == but1:
		#newX = (coordx-1)%8
		pass
	elif channel == but2:
		coordy = (coordy-1)%8
	elif channel == but3:
		coordy = (coordy+1)%8
	refreshScreen()

print("Etch A Sketch:\nTo Play: Use knobs to move and the rightmost button to clear.\nPress ctrl+C to quit.")

bus.write_byte_data(matrix, 0x21, 0) #Start oscillator
bus.write_byte_data(matrix, 0x81, 0) #Disp on, blink off
bus.write_byte_data(matrix, 0xe7, 0) #Full brightness
time.sleep(0.1)

refreshScreen()
GPIO.add_event_detect(but0, GPIO.RISING, callback=detectedInput)
GPIO.add_event_detect(but1, GPIO.RISING, callback=detectedInput)
GPIO.add_event_detect(but2, GPIO.RISING, callback=detectedInput)
GPIO.add_event_detect(but3, GPIO.RISING, callback=detectedInput)
while True:
	if (hEncoder.position != hPos):
		if (hEncoder.position > hPos):
			coordx = (coordx+1)%8
		else:
			coordx = (coordx-1)%8
		refreshScreen()
		time.sleep(0.05)
		hPos = hEncoder.position

	elif (vEncoder.position != vPos):
		if (vEncoder.position > vPos):
			coordy = (coordy+1)%8
		else:
			coordy = (coordy-1)%8
		refreshScreen()
		time.sleep(0.05)
		vPos = vEncoder.position
