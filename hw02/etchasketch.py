#!/usr/bin/env python3

import sys
import curses
from curses import wrapper
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

coordx = 1
coordy = 1
pad = 0

def resetScreen(pad):
	pad.addch(0,0,' ')
	stdscr.refresh()
	n=0
	while (n<gridSize):
		pad.addch(n+48)
		n=n+1
	n=0
	while (n<gridSize):
		pad.addch(n+1,0,n+48)
		n=n+1
	pad.refresh(0,0, 0,0, lines, cols)
	pad.move(coordy, coordx)

def detectedInput(channel):
	global coordy
	global coordx
	global pad
	newY = coordy
	newX = coordx
	if channel == but0:
		time.sleep(1)
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
	try:
		pad.addch(newY,newX,'X')
	except curses.error as e:
		pass
	pad.move(newY,newX)
	coordy = newY
	coordx = newX
	pad.refresh(0,0, 0,0, lines,cols)

def main(stdscr):
	global pad
	# Clear screen
	stdscr.clear()
	pad = curses.newpad(int(gridSize)+1, int(gridSize)+1)
	lines = gridSize+1
	if (curses.LINES-1 < lines):
		lines = curses.LINES-1
	cols = gridSize+1
	if (curses.COLS-1 < cols):
		cols = curses.COLS-1
	resetScreen(pad)
	pad.move(1,1)
	pad.refresh(0,0, 0,0, lines,cols)
	#curs_set(False)
	#coordy = 1
	#coordx = 1
	c = 0
	GPIO.add_event_detect(but0, GPIO.RISING, callback=detectedInput)
	while True:
		c = stdscr.getch()
		if (c == ord(' ')):
			pad.clear()
			resetScreen(pad)
		if (c == ord('q')):
			break

gridSize = 8
lines = 0
cols = 0

if (len(sys.argv) >= 2):
	gridSize = int(sys.argv[1])
print("Etch A Sketch:\nRun './etchasketch.py X' to run with custom size 'X' (default is 8).\nTo Play: Use arrow keys to move and 'space' to clear.\nPress 'q' to quit.")
time.sleep(7)
stdscr = curses.initscr()
wrapper(main)
curses.endwin()
