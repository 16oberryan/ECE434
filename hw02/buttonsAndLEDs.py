#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

but0 = "P9_22"
but1 = "P9_21"
but2 = "P9_18"
but3 = "P9_17"
LED0 = "P9_31"
LED1 = "P9_29"
LED2 = "P9_30"
LED3 = "P9_28"

GPIO.setup(LED0, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(but0, GPIO.IN)
GPIO.setup(but1, GPIO.IN)
GPIO.setup(but2, GPIO.IN)
GPIO.setup(but3, GPIO.IN)

#while True:
	#GPIO.output(LED0, GPIO.input(but0))
# Map buttons to LEDs
map = {but0: LED0, but1: LED1, but2: LED2, but3: LED3}

def updateLED(channel):
	state = GPIO.input(channel)
	GPIO.output(map[channel], state)

GPIO.add_event_detect(but0, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(but1, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(but2, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(but3, GPIO.BOTH, callback=updateLED)

try:
	while True:
		time.sleep(100)

except KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()
