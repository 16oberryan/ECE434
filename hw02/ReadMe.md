The Etch A Sketch program now works with buttons, although since I only have four buttons, there is currently no clear functionality.
I used curses previously, and couldn't get it to work with the buttons, so instead of trying to force it, I rewrote the program in a way that will make it easier to move to the LED grid. However, this did lead to a significant downgrade in quality while it's still using the terminal (it re-prints the grid every update). There is also no longer any keyboard input, only push-buttons.
Etchasketch is still run with './etchasketch.py X' (where X is the grid size)

Oscilloscope measurements

x  |  min (V)	|  max (V)	| period (ms)	|processor usage|shortest period	|processor at shortest period
--|  -------    |  -------  | -----------   | --------------|---------------    |----------------------------
bash	|  -2.5V	|  1.9V		| 240 ms	| 19%		| 36ms			| 100%
sh	|  -2.5V	|  1.9V		| 226 ms	| 13%		| 26ms			| 100%
python	|  -2.4V	|  1.8V		| 202 ms	| 2%		| 360 us		| 80%
C	|  -2.4V	|  1.8V		| 202 ms	| 2%		| 300 us		| 65%

100 ms is actually the half-period in the code, so the period when the input is 0.1s is 200, which is still off significantly for bash and sh, but is pretty close with python and C
Using bash, sh, and python, the period is fairly stable, with occasional long pulses. In C it appears to be perfectly stable
When launching vi, in bash, sh, and python, the wave had a series of longer pulses (more noticeable with shorter periods). In C, there was no variation (that I noticed)
After removing some unnecessary lines in the .sh script, the period got closer to the correct period, at ~213ms (using sh) and 13 ms was the shortest possible period
