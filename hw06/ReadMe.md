#Homework 6

##Video questions
1) Julia works for National Instruments
2) PREEMT_RT is a way of preempting basically the entire OS to respond to a signal immediately with very little overhead
3) Mixed criticality is when a system is running multiple tasks, some of which might require real time responses, others might not be as time critical. These tasks may need to communicate, or at least run together.
4) Drivers can misbehave by continuing to run tasks even if higher priority tasks have been given.
5) Delta is the time it takes from the moment the event occurs until the relevant tasks actually execute
6) Cyclictest is a way of testing the delay of real time responses. One thread takes a timestamp, then sleeps for a set amount of time. Then it takes another timestamp. The difference between the timestamps should be the expected delay plus the delay it took to respond to a stimuli (assuming an event occured in that time)
7) The purple is a graph of activity of a response to an event using an OS preempting method. The green is the same, but using real time preempting methods (PREEMPT_RT)
8) Dispatch latency is the time it take for the hardware to respond to the event and send the interrupt signal to wake up the relevant thread. Scheduling latency is the time it takes from the moment the scheduler is aware of the event (the interrupt) to the moment the CPU is given the code to begin execution
9) Mainline is a type of diagram used to show tasks of different priorities. The x-axis is time, and tasks are shown with higher priority tasks being higher on the diagram. Arrows are included to show interrupts.
10) The lower priority interrupt is keeping the external event from starting.
11) The Real Time patch puts very little code in the interrupt handler, so that any code that would've been in the interrupt handler previously can now be interrupted, which lets high priority tasks run right away.

