# -*- coding: cp1252 -*-
"""
File:           lesson_14_UseThreadingBaseClass.py

Description:    This script demonstrates the use of the dSPACE Threading base class.

Preconditions:  -
                
Tip/Remarks:    -

Limitations:    -

Version:        3.0

Date:           May 2013

                dSPACE GmbH shall not be liable for errors contained herein or
                direct, indirect, special, incidental, or consequential damages
                in connection with the furnishing, performance, or use of this
                file.
                Brand names or product names are trademarks or registered
                trademarks of their respective companies or organizations.

Copyright (c) 2013 by dSPACE GmbH
"""

from win32com.client import Dispatch
# Import threading base class.
from dspace.com.threads import STAThread, MTAThread
# Import the Sleep command to suspend any thread for a certain amount of time.
from win32api import Sleep
import threading
import pythoncom

# Initialize global variable for thread synchronization.
STOP = 0

#--------------------------------------------------------------------------------------------------
# Function ExecuteLesson:
#   This function runs the lesson.
#--------------------------------------------------------------------------------------------------
def ExecuteLesson():
    WScript = Dispatch("wscript.shell")
    
    # Open webpage in Internet Explorer.
    IEApplication = Dispatch('internetexplorer.application')
    IEApplication.Visible = 1
    
    InternetThread = STAThread(NavigateToPage, 'Navigation', (IEApplication, 'www.google.com'))
    InternetThread.start()
    
    PrintCurrentDirectoryThread = STAThread(PrintCurrentDirectory, args=(WScript,))
    PrintCurrentDirectoryThread.start()

    UnknownObject = WScript._oleobj_.QueryInterface(pythoncom.IID_IUnknown)
    UnknownObjectThread = STAThread(PrintUnknownObject, 'UnknownObjectThread', kwargs={'unknownObject':UnknownObject})
    UnknownObjectThread.start()
    
    PrintDOMElementsThread = STAThread(PrintDOMElements, 'DOMElements', (IEApplication,))
    PrintDOMElementsThread.start()
    
    PrintMultiArgsThread = STAThread(PrintMultipleArguments, args=(WScript, 'MyTestString'), name='MultipleArgumentsThread')
    PrintMultiArgsThread.start()
    
    # Create the two threading objects using the threading base class.
    FirstThread = MTAThread(target=ThreadStopFunc, args=())
    SecondThread = MTAThread(target=ThreadFunc, name='SecondThread')
    
    # Start the threads.
    FirstThread.start()
    SecondThread.start()
    
    # Print the number of threads running including the main thread.
    print "Number of threads running : %i\n"  % threading.activeCount(),

#--------------------------------------------------------------------------------------------------
# Function PrintCurrentDirectory:
#   This function is for the thread which print the current directory.
#--------------------------------------------------------------------------------------------------
def PrintCurrentDirectory(wscript):
    print "The current directory is: %s" % wscript.CurrentDirectory,

#--------------------------------------------------------------------------------------------------
# Function PrintDOMElements:
#   This function is for the thread which print the DOM elements.
#--------------------------------------------------------------------------------------------------
def PrintDOMElements(application):
    print "These are the text element in the DOM:\n",
    # Wait for the document to finish loading
    READYSTATE_COMPLETE = 4
    while application.ReadyState != READYSTATE_COMPLETE:
        Sleep(100)
    for element in application.Document.documentElement.all:
        if element.toString() != "[object]":
            print "%s\n" % element,

#--------------------------------------------------------------------------------------------------
# Function PrintMultipleArguments:
#   This function is for the thread which print the multiple arguments.
#--------------------------------------------------------------------------------------------------
def PrintMultipleArguments(wscript, myString):
    print "This is a string: %s\n" % myString,
    print "The current directory is: %s\n" % wscript.CurrentDirectory,

#--------------------------------------------------------------------------------------------------
# Function NavigateToPage:
#   This function is for the thread which navigate to a specified webpage in Internet Explorer.
#--------------------------------------------------------------------------------------------------
def NavigateToPage(app, destinationPage):
    print app
    print "Navigated to page: %s\n" % destinationPage,
    # if input argument to thread class was 'IEApplication', use app.Navigate(..)
    # if input argument to thread class was 'IEApplication._oleobj_', use app2 = Dispatch(app), app2.Navigate(..)
    app2 = Dispatch(app)
    app2.Navigate(destinationPage)

#--------------------------------------------------------------------------------------------------
# Function PrintUnknownObject:
#   This function is for the thread which prints the unkonwn object.
#--------------------------------------------------------------------------------------------------
def PrintUnknownObject(unknownObject):
    print "Unknown Interface: %s\n" % unknownObject,
    wscript = Dispatch(unknownObject.QueryInterface(pythoncom.IID_IDispatch))
    print "The current directory is: %s\n" % wscript.CurrentDirectory,

#--------------------------------------------------------------------------------------------------
# Function ThreadStopFunc:
#   This function is for the thread which waits for five seconds and then stops the second
#   afterwards.
#--------------------------------------------------------------------------------------------------
def ThreadStopFunc():
    # Use the global variable STOP.
    global STOP
    
    # Wait for three seconds.
    Sleep(3000)
    
    # Stop the other thread by setting the global variable.
    print "Stopping Thread\n",
    
    STOP = 1

#--------------------------------------------------------------------------------------------------
# Function ThreadFunc:
#   This function .
#--------------------------------------------------------------------------------------------------
def ThreadFunc():
    # Use the global variable STOP.
    global STOP

    # Start the loop which would block the main thread.
    # This loop should check always the global variable.
    Index = 0
    
    while STOP == 0:
        print "Current counter for stop function %d\n" % Index,
        Index = Index + 1
        # Stop this thread to let other threads run.
        # If you don't include the Sleep function the other threads aren't given time to run.
        Sleep(100)
        
    print "Thread Stopped\n",
    
# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()