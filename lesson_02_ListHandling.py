# -*- coding: cp1252 -*-
"""
File:           lesson_02_ListHandling.py

Description:    This script demonstrates basic features of list handling.

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
   
    # Construct an empty list.
    MixedElements = []
    
    # Append string elements to the list.
    MixedElements.append("Default String")
    MixedElements.append(12)
    MixedElements.append(4.0)
    MixedElements.append(True)
    MixedElements.append(12)
    MixedElements.append(u"Unicode String")
    
    # Print mixed list.
    print MixedElements
    
    # Construct a new integer list.
    IntegerElements = [1, 0, 7, -4]
    
    # Print concatenated lists.
    print MixedElements + IntegerElements
    
    # Include a list as a list element
    MixedElements.append(IntegerElements)
    
    # Print mixed list.
    print MixedElements
    
    # Insert element at given position.
    MixedElements.insert(2, "New Element")
    
    # Print mixed list.
    print MixedElements
    
    # Remove element with value 4.0.
    MixedElements.remove(4.0)
    
    # Print mixed list.
    print MixedElements
    
    # Pop element at position 5.
    print MixedElements.pop(5)
    
    # Print mixed list.
    print MixedElements
    
    # Sort integer list.
    IntegerElements.sort()
    
    # Print sorted integer list.
    print IntegerElements
    
    # Sort integer list reverse.
    IntegerElements.sort(reverse=True)
    
    # Print reverse sorted integer list.
    print IntegerElements

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()