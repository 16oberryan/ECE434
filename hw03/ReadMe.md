When readTemp.py is run, it will read the temperature from the temp101 sensor and convert it to Fahrenheit before printing the value
The etchasketch program now runs on the LED grid and is controlled by two rotary sensors (It is notable that P8_41 and P8_42 didn't work correctly for QEP with the rotary encoders for some reason. Maybe only one pin was malfuctioning)

In order for the programs to run properly, you must first run setup.sh to configure the pins

## Prof. Yoder's comments

etch_a_sketch looks good.  THe Alert part is missing from the TMP101.

Grade:  9/10