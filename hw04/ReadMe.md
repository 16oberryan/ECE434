*Homework 4

**Memory Map
I recreated the memory map for the BeagleBone Black (memoryMap.pdf) as instructed

**GPIO via mmap
1. I have wired it up so that two buttons (connected to pins P9_11 and P9_12) toggle two LEDs (USR2 and USR3). The program runs for 15 seconds then quits.
2. I wrote a program to toggle gpio pin P8_16 (togglePin.c) that uses mmap, and my results are as follows:
Fastest period with usleep: 160us
Fastest peroid without usleep: 350ns
Previously, the shortest period I'd seen was 300 us in C, but with mmap, it got significantly faster.

**2.4" TFT LCD Display

