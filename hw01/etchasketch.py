import sys
import curses
from curses import wrapper
import time

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

def main(stdscr):
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
	coordy = 1
	coordx = 1
	c = 0
	while (c != ord('q')):
		c = stdscr.getch()
		newY = coordy
		newX = coordx
		if c == curses.KEY_RIGHT:
			newX = coordx+1
			if newX == gridSize+1:
				newX = 1
		elif c == curses.KEY_LEFT:
			newX = coordx-1
			if newX == 0:
				newX = gridSize
		elif c == curses.KEY_UP:
			newY = coordy-1
			if newY == 0:
				newY = gridSize
		elif c == curses.KEY_DOWN:
			newY = coordy+1
			if newY == gridSize+1:
				newY = 1
		elif c == ord(' '):
			pad.clear()
			resetScreen(pad)
		else:
			continue
		try:
			pad.addch(newY,newX,'X')
		except curses.error as e:
			pass
		pad.move(newY,newX)
		coordy = newY
		coordx = newX
		pad.refresh(0,0, 0,0, lines,cols)

gridSize = 8
lines = 0
cols = 0

if (len(sys.argv) >= 2):
	gridSize = int(sys.argv[1])
print("Etch A Sketch:\nRun 'python etchasketch.py X' to run with custom size 'X' (default is 8).\nTo Play: Use arrow keys to move and 'space' to clear.\nPress 'q' to quit.")
time.sleep(7)
stdscr = curses.initscr()
wrapper(main)
curses.endwin()
