#Drashaun Morrow
#This program will use multiprocessing to run a function multiple times



import multiprocessing
import random
import time
from datetime import datetime

def waitToPrint():
    # Wait for a random number of seconds between 0 and 1
    time.sleep(random.uniform(0, 1))
    # Print the current time
    print(f"Current time is {datetime.now()}")
    
if __name__ == '__main__':
    # Create three separate processes
    processes = []
    for i in range(3):
        printTime = multiprocessing.Process(target=waitToPrint)
        processes.append(printTime)
        printTime.start()

    # Wait for all processes to finish
    for printTime in processes:
        printTime.join()