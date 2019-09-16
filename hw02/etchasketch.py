#!/usr/bin/env python3

import sys
import time
import Adafruit_BBIO.GPIO as GPIO

but0 = "P9_22"
but1 = "P9_21"
but2 = "P9_18"
but3 = "P9_17"
GPIO.setup(but0, GPIO.IN)
GPIO.setup(but1, GPIO.IN)
GPIO.setup(but2, GPIO.IN)
GPIO.setup(but3, GPIO.IN)

gridSize = 8
lines = 0
cols = 0

if (len(sys.argv) >= 2):
	gridSize = int(sys.argv[1])

coordx = 1
coordy = 1
screen = [[None for x in range(gridSize+1)] for y in range(gridSize+1)]

def resetScreen():
	i = 0
	print("")
	while (i<=gridSize):
		j = 0
		while(j<=gridSize):
			print(screen[i][j], end='')
			j+=1
		print("")
		i+=1

def detectedInput(channel):
	global coordy
	global coordx
	newY = coordy
	newX = coordx
	if channel == but0:
		newX = coordx+1
		if newX == gridSize+1:
			newX = 1
	elif channel == but1:
		newX = coordx-1
		if newX == 0:
			newX = gridSize
	elif channel == but2:
		newY = coordy-1
		if newY == 0:
			newY = gridSize
	elif channel == but3:
		newY = coordy+1
		if newY == gridSize+1:
			newY = 1
	screen[newX][newY] = 'X'
	coordy = newY
	coordx = newX
	resetScreen()

print("Etch A Sketch:\nRun './etchasketch.py X' to run with custom size 'X' (default is 8).\nTo Play: Use buttons to move and be sad if you want to clear.\nPress ctrl+C to quit.\n(It may help to shrink your terminal window to the size of the board)")
time.sleep(2)
screen[0][0] = ' '
n = 0
while (n < gridSize):
	screen[n+1][0] = n
	screen[0][n+1] = n
	n+=1
i = 1
while (i <= gridSize):
	j = 1
	while (j <= gridSize):
		screen[i][j] = ' '
		j+=1
	i+=1
resetScreen()
GPIO.add_event_detect(but0, GPIO.RISING, callback=detectedInput)
GPIO.add_event_detect(but1, GPIO.RISING, callback=detectedInput)
GPIO.add_event_detect(but2, GPIO.RISING, callback=detectedInput)
GPIO.add_event_detect(but3, GPIO.RISING, callback=detectedInput)
while True:
	pass
