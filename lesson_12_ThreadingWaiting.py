# -*- coding: cp1252 -*-
"""
File:           lesson_12_ThreadingWaiting.py

Description:    This script shows how to synchronize different threads
                of execution by using a lock object.

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

#--------------------------------------------------------------------------------------------------
# This function is the executable object for the first thread.
#--------------------------------------------------------------------------------------------------
def ThreadOne(Lock):
    print "Thread one waiting ..."
  
    # Try to acquire the lock. As long as this thread could not acquire the lock it stops.
    Lock.acquire()
    
    # The operations should be surrounded by a try except block to be sure that the lock will be released.
    try:
        # Print message that the thread is running.
        print "Thread one running ..."
        
        # Print the numbers from 0 to 9 with a sleeping time of 100 ms in between.
        for Index in range(10):
            print "Thread one at index: %i" % Index
            Index = Index + 1
            Sleep(100)
    
        # Print message that the thread has stopped.
        print "Thread one stopped!"
    except:
        pass
    
    finally:
        # Release the lock and let other threads run.
        Lock.release()

#--------------------------------------------------------------------------------------------------
# Function : ThreadTwo
#      This function is the executable object for the second thread.
#--------------------------------------------------------------------------------------------------
def ThreadTwo(Lock):
    print "Thread two waiting ..."
    
    # Try to acquire the lock. As long as this thread could not acquire the lock it stops.
    Lock.acquire()
    
    # The operations should be surrounded by a try except block to be sure that the lock will be released.
    try:
        # Print message that the thread is running.
        print "Thread two running ..."
        
        # Print the numbers from 0 to 9 with a sleeping time of 100 ms in between.
        for Index in range(10):
            print "Thread two at index: %i" % Index
            Index = Index + 1
            Sleep(100)
    
        # Print message that the thread has stopped.
        print "Thread two stopped!"
    
    except:
        pass
    
    finally:
        # Release the lock and let other threads run.
        Lock.release()

#--------------------------------------------------------------------------------------------------
# Function : ThreadTwo
#      This function runs in the main thread and creates the two other threads.
#--------------------------------------------------------------------------------------------------
def ExecuteLesson():
    # Print message that the main thread is running.
    print "MainThread running ..."
    
    # Create a lock object to synchronize the two created threads.
    Lock = threading.Lock()

    # Create the two thread objects.
    FirstThread   = threading.Thread(target=ThreadOne, args =(Lock,))
    SecondThread   = threading.Thread(target=ThreadTwo, args =(Lock,))

    # Start the two threads.
    FirstThread.start()
    SecondThread.start()

    # Print the number of threads running this should be three: main, first and second thread.
    print "Number of threads running: %i" % threading.activeCount()

    # Print message that the main thread is waiting for the first thread to stop.
    print "MainThread waiting for thread one ..."
    
    # With the join functions the main thread waits for the first thread to be finished.
    FirstThread.join()

    # Print message that the main thread is waiting for the second thread to stop.
    print "MainThread waiting for thread two ..."
    
    # With the join functions the main thread waits for the second thread to be finished.
    SecondThread.join()

    # Print message that the main thread has stopped.
    print "MainThread stopped!"

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()
