# -*- coding: ascii -*-
"""
File:        RTTSequence.py

Description: Module which provides the tests for real-time testing
             functions to be executed on real-time hardware.

Tip/Remarks: -

Limitations: -

Version:     2.0

Date:        2013-05-28

             dSPACE GmbH shall not be liable for errors contained herein or
             direct, indirect, special, incidental, or consequential damages
             in connection with the furnishing, performance, or use of this
             file.
             Brand names or product names are trademarks or registered
             trademarks of their respective companies or organizations.

Copyright (c) 2013 by dSPACE GmbH
"""

#-----------------------------------------------------------------------------
# Import all classes from the rttlib module.
# This Python library provides all real-time testing modules.
# All imports must be defined in the global part of the script.
#-----------------------------------------------------------------------------
from rttlib import variable
from rttlib import utilities
from rttlib import datastream

#------------------------------------------------------------------------------
# Module global variables
#------------------------------------------------------------------------------

# Create variable objects for accessing Simulink signals
currentTime        = utilities.currentTime

# the variable description for this application is a TRC file
Micro1 = variable.Variable(r'Model Root/Inputs/Micro1/Value')
Micro2 = variable.Variable(r'Model Root/Inputs/Micro2/Value')

matFileName    = ''

#------------------------------------------------------------------------------
# Read sequence argument passed to sequences.Create()
#------------------------------------------------------------------------------
try:
    sequenceArgument = utilities.GetSequenceArgument()

    # Check for optional arguments
    if sequenceArgument:
        if    isinstance(sequenceArgument, str) \
           or isinstance(sequenceArgument, unicode):
            # Get the name of the MAT file
            matFileName = sequenceArgument
            
        else:
            raise Exception("Sequence argument is not a string.")
except:
    raise Exception("Sequence argument is missing. Start the sequence with"\
                     " the script 'RTTLoader.py'.")

# Map variable objects to the MAT file variables
# The constructor uses the MAT file time variable name
variablesToStimulate = datastream.CreateVariableMap("Time")

# All variables objects must be mapped to a MAT file variable name.
variablesToStimulate.AddVariable("Signal_1", Micro1)
variablesToStimulate.AddVariable("Signal_2", Micro2)


# Create a data stream
myStream = datastream.MatFile(matFileName, variablesToStimulate)

# Identifier for real-time testing print messages
rttPrefix = r" *RTT:* "

def MainGenerator():

    """
     Function: MainGenerator
         This function is the main real-time testing generator function.
         The name of the function is mandatory because it is the defined
         entry point for the script scheduler.
    """
    print rttPrefix + "Start of real-time test execution on target platform"

    yield None

    print rttPrefix + "Start data streaming at '%0.6f' " % currentTime.Value

    # Start the data replay
    yield myStream.Replay()

    yield None
    print rttPrefix + "Start data streaming again at '%0.6f' " \
          % currentTime.Value

    # Start the data replay again
    yield myStream.Replay()

    print rttPrefix + "Finished data streaming at '%0.6f' " % currentTime.Value

    yield None

    print rttPrefix + "End of real-time test execution."

