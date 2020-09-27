# -*- coding: cp1252 -*-
"""
File:           lesson_11_ThreadingBasics.py

Description:    This script shows how to stop a thread from another thread
                using the threading module to start the threads.

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

# Initialize global variable for thread synchronization.
STOP = 0

#--------------------------------------------------------------------------------------------------
# Function : ThreadStopFunc
#      Thread which waits for five seconds and then stops the second afterwards.
#--------------------------------------------------------------------------------------------------
def ThreadStopFunc():
    # Use the global variable STOP.
    global STOP
    
    # Wait for five seconds.
    Sleep(5000)
    
    # Stop the other thread by setting the global variable.
    print "Stopping Thread"
    STOP = 1

#--------------------------------------------------------------------------------------------------
# Function : ThreadFunc
#      Thread function which is running.
#--------------------------------------------------------------------------------------------------
def ThreadFunc():
    # Use the global variable STOP.
    global STOP

    # Start the loop which would block the main thread.
    # This loop should check always the global variable.
    Index = 0
    
    while STOP == 0:
        print Index
        Index = Index + 1
        # Stop this thread to let other threads run.
        # If you don't include the Sleep function the other threads aren't given time to run.
        Sleep(100)
        
    print "Thread Stopped"


#--------------------------------------------------------------------------------------------------
# Function : ExecuteDemo
#      Demo function which starts the threads.
#--------------------------------------------------------------------------------------------------
def ExecuteLesson():
    # Create the two threading objects.
    FirstThread = threading.Thread(target=ThreadStopFunc, args =())
    SecondThread = threading.Thread(target=ThreadFunc, args =())

    # Start the threads.
    FirstThread.start()
    SecondThread.start()

    # Print the number of threads running this should be three: main, first and second thread.
    print "Number of threads running : %i"  % threading.activeCount()

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()
