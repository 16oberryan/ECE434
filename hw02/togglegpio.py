#!/usr/bin/env python3

import sys
import time
import Adafruit_BBIO.GPIO as GPIO

pin = "P9_12"

GPIO.setup(pin, GPIO.OUT)
delay = float(sys.argv[1])

while True:
	GPIO.output(pin, 1)
	time.sleep(delay)
	GPIO.output(pin, 0)
	time.sleep(delay)
