# -*- coding: ascii -*-
"""
File:        RTTLoader.py

Description: This script shows how to download a real-time testing script on a
             platform with a running application.

Tip/Remarks: To test the script download with a demo application, run
             the script 'StartDemo.bat'
             Run this script afterwards.

Limitations: -

Version:     2.0

Date:        2013-05-28

             dSPACE GmbH shall not be made liable for errors contained herein
             or direct, indirect, special, incidental, or consequential damages
             in connection with the furnishing, performance, or use of this
             file.
             Brand names or product names are trademarks or registered
             trademarks of their respective companies or organizations.

Copyright (c) 2013 by dSPACE GmbH
"""

# Host script: print allowed
#pylint:disable-msg=W2000

#-----------------------------------------------------------------------------
# Import real-time testing modules
#-----------------------------------------------------------------------------
# This Python library is used to handle the test script download.
import rttmanagerlib

# This Python library is used to generate byte code from Python test files.
import rttbytecodegenerator

# This Python library provides utility functions.
import rttutilities

#-----------------------------------------------------------------------------
# Import this module for accessing the Python COM automation API.
#-----------------------------------------------------------------------------
import pythoncom

#-----------------------------------------------------------------------------
# Use the standard Python built-in libraries for operation-system commands.
#-----------------------------------------------------------------------------
import os
import sys

#------------------------------------------------------------------------------
# Module global variables
#-------------------------------------------------------------------------------

workingDir = 'C:\\Users\\1vigneni\\Desktop\\workfolder\\16_TestOnRealModel'
testScriptName    = workingDir + r'\Model\LockIn_RTT\Experiment_001\Python Scripts\RTTSequence.py'
matFilename       = workingDir + r'\Model\LockIn_RTT\Global Data Sets\DataStreaming_3.mat'

#-----------------------------------------------------------------------------
# Import real-time testing demo utilities.
#-----------------------------------------------------------------------------
import rttdemoutilities


def executeDemo(boardName):
    """
     Function : executeDemo
         Execute part of the demo.
    """

    # Generate byte code from the test script (RTT sequence)
    bcgFileName = rttbytecodegenerator.Generate(testScriptName)
    print "BCG file created: ", bcgFileName

    # Create new sequence
    rttManager = rttmanagerlib.RealTimeTestManagerServer()
    board = rttManager.AccessBoard(boardName)
    print "Board '%s' successfully connected." % board.Name
    
    # Connect to sequence's event handle
    sequencesEvents = rttdemoutilities.RTTMSequencesEvents(board.Sequences)
    try:
        # Load a sequence to the real-time platform
        sequence = board.Sequences.Create(bcgFileName, matFilename)
        print "Sequence '%s' on real-time platform created. " % bcgFileName

        # Start the sequence on the real-time platform
        sequence.Run()
        print "Sequence on real-time platform started.\n"

        # Suspend host script for the execution time of the real-time testing
        # script
        numberOfSeconds = 2
        print "\nSuspend host script execution for %d seconds." \
              % numberOfSeconds
        rttutilities.RTTSleep(numberOfSeconds)


    finally:
        # Clear traceback object to free COM object
        sys.last_traceback = None

        # Clean up
        if sequencesEvents:
            sequencesEvents.close()
            sequencesEvents = None
        sequence   = None
        board      = None
        rttManager = None


#-----------------------------------------------------------------------------
# Main Program
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    if (2 == len(sys.argv)):
        # The script execution is started in python.exe.
        if "python.exe" in sys.executable.lower():
            # Python.exe does not call the COM initialization method.
            # Initialize the COM libraries for the calling thread.
            pythoncom.CoInitialize()

        try:
            board = sys.argv[1]

            print "\nThe real-time testing DataStreaming is starting..."

            executeDemo(board)

            print "\nThe real-time testing DataStreaming was successfully "\
                  "completed."

        finally:
            # The script execution is started in python.exe.
            if "python.exe" in sys.executable.lower():
                # Python.exe does not call the COM uninitialization method.
                # Uninitialize the COM libraries for the calling thread.
                pythoncom.CoUninitialize()

    else:
        print "No platform defined."
        print "Usage with DS100X-Boards:   'RTTLoader.py DS100X'"
        print "Usage with IP-Address:      'RTTLoader.py <IP-Address>/<real-time application name>'"
