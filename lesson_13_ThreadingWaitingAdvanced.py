# -*- coding: cp1252 -*-
"""
File:           lesson_13_ThreadingWaitingAdvanced.py

Description:    This script shows how to wait in the main thread for other
                threads which are executed.

Tip/Remarks:    -

Limitations:    -

Version:        1.0

Date:           Mar 2009

                dSPACE GmbH shall not be made liable for errors contained herein or
                direct, indirect, special, incidental, or consequential damages
                in connection with the furnishing, performance, or use of this
                file.
                Brand names or product names are trademarks or registered
                trademarks of their respective companies or organizations.

Copyright (c) 2009 by dSPACE GmbH
"""
# Import the threading library which grants a higher level access to threads.
import threading

# Import the Sleep command to suspend any thread for a certain amount of time.
from win32api import Sleep

import pythoncom

#--------------------------------------------------------------------------------------------------
# Function : ThreadFunction
#      This function is the executable object for all thread.
#--------------------------------------------------------------------------------------------------
def ThreadFunction():
    # Do the thread loop and identify the print output by the thread name.
    print "Thread running ... %s" % threading.currentThread().getName()
    
    # Print the numbers from 0 to 9 with a sleeping time of 100 ms in between.
    for Index in range(10):
        print "%s at index  %d" % (threading.currentThread().getName(), Index)
        Index = Index + 1
        Sleep(100)

#--------------------------------------------------------------------------------------------------
# Function : WaitForAllThreads
#      This function waits for all thread created to be finished.
#--------------------------------------------------------------------------------------------------
def WaitForAllThreads():
    # Retrieve all created threads.
    Threads = threading.enumerate()
    
    while threading.activeCount() > 1:
            
        # Pump all waiting messages of the current thread.
        pythoncom.PumpWaitingMessages()
        
        Sleep(100)

#--------------------------------------------------------------------------------------------------
# Function : ExecuteDemo
#      This function runs in the main thread and creates ten threads.
#--------------------------------------------------------------------------------------------------
def ExecuteLesson():
    # Create ten thread objects.
    Threads = []
    for Index in range(10):
        Threads.append(threading.Thread(target=ThreadFunction))

    # Start all threads.
    for Thread in Threads:
        print Thread.getName()
        Thread.start()

    # Print the number of threads running.
    print "Number of threads running: %i" % threading.activeCount()

    # Wait in the main thread for threads to be finished.
    WaitForAllThreads()
    
    # Print message that the main thread has stopped.
    print "MainThread stopped!"

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()
