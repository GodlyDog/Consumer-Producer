Consumers and producer run in separate threads, with the main thread retaining
control of the program. (5 threads in total)

To run, run main.py either from IDE or terminal. The program will
run until stopped, continuously adding to and removing from queues.
To stop the program cleanly, send SIGINT to the running process (control + c).
The program listens for SIGINT to join the active threads and shutdown.
If running in an IDE terminal like Jetbrains IDEs, the stop button on the side
of the terminal usually sends SIGINT. Other signals will also stop the running 
process, but not cleanly.

Python v3.9
