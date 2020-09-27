# -*- coding: cp1252 -*-
"""
File:           lesson_05_SequenceHandling.py

Description:    This script demonstrates features of general sequence handling (e.g. tuple and list).

Preconditions:  -
                
Tip/Remarks:    -

Limitations:    -

Version:        1.0

Date:           Mar 2009

                dSPACE GmbH shall not be liable for errors contained herein or
                direct, indirect, special, incidental, or consequential damages
                in connection with the furnishing, performance, or use of this
                file.
                Brand names or product names are trademarks or registered
                trademarks of their respective companies or organizations.

Copyright (c) 2009 by dSPACE GmbH
"""
#--------------------------------------------------------------------------------------------------
# Function ExecuteLesson:
#   This function runs the lesson.
#--------------------------------------------------------------------------------------------------
def ExecuteLesson():
   
    # Construct three different sequences.
    StringSequence = "Default"
    ListSequence = [1, "DefaultString", True, 5, 4.0, 14, "i"]
    TupleSequence = (3, 56, 8, "Hi")
   
    # All methods will be executed with the two sequences. So iterate over the sequences.
    for CurrentSequence in [StringSequence, ListSequence, TupleSequence]:
        
        print "Start new sequence: " 
        
        # Print current sequence.
        print CurrentSequence
        
        # Print number of elements.
        print len(CurrentSequence)
         
        # Check if "i" is an element of the sequence.
        print "i" in CurrentSequence
        
        # Iterate over the elements.
        for CurrentElement in CurrentSequence:
            
            # Print current element.
            print "Element: %s of type: %s" % (CurrentElement, type(CurrentElement))
        
        # Print the minimum element.
        print min(CurrentSequence) 
        
        # Print the maximum element.
        print max(CurrentSequence) 
         
        # Take the first element.
        print CurrentSequence[0]
         
        # Take only the four last elements.
        print CurrentSequence[-4:]
         
        # Take only two elements starting with a given index.
        print CurrentSequence[-4:-2]
         
        # Take all elements except the four last.
        print CurrentSequence[:-4]
    
    # Iterate over two sequences in at once.
    for FirstSequenceElement, SecondSequenceElement in zip(StringSequence, ListSequence):
        print "%s, %s" % (FirstSequenceElement, SecondSequenceElement)
    
    # Iterate over a list with index.
    for Index, CurrentElement in enumerate(StringSequence):
        print "%s, %s" % (Index, CurrentElement) 

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()