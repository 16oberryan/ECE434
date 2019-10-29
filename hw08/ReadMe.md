#Homework 8

##2.6 Blinking an LED
The command to start the PRU code in the Makefile is 'make start', likewise, the command to stop it is 'make stop'
The fastest the pin toggles is 12.5 MHz (period of 80ns). The signal isn't a perfect square wave (there is overshoot and some oscillation, and when it starts settling, it changes), but it is reasonably stable with only occasional hiccups.

##5.3 PWM Generator
The waveform looks more stable, with a std dev down to 142ps (about half the previous section's std dev). There doesn't appear to be any jitter.

##5.4 Controlling the PWM Frequency
The output pins being driven are pins P9_28,  P9_29,  P9_30, and  P9_31. Bits 0, 1, 2, and 3 are used in __R30. The highest frequency is 326.8kHz (3.06us period). There isn't any obvious jitter.
pwm-test.c does successfully change the on and off times.

##5.9 Reading an Input at Regular Intervals
The code causes the output signal to be delayed by 30ns.

##Table

| value                  | blink led | PWM generator | controlling PWM | reading input |
|------------------------|-----------|---------------|-----------------|---------------|
| fastest frequency/time | 12.5 MHz  | 142ps std dev | 326.8kHz        | 30ns delay    |
