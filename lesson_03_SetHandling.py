# -*- coding: cp1252 -*-
"""
File:           lesson_03_SetHandling.py

Description:    This script demonstrates basic features of sets.

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
   
    # Construct an empty set.
    FirstElements = set()
    
    # Add a new element.
    FirstElements.add(23)
    
    # Print set.
    print FirstElements
    
    # Add some elements.
    FirstElements.add(23)
    FirstElements.add("Default String")
    FirstElements.add(True)
    FirstElements.add(23)
    FirstElements.add(4.0)
    FirstElements.add("Other String")
    
    # Print set. All elements are unique.
    print FirstElements
    
    # Construct a second set.
    SecondElements = set(["Default String", False, 4.0, "Test", 15])
    
    # Print second set.
    print SecondElements
    
    # Print union of both sets. Is equivalent to FirstElements.union(SecondElements).
    print FirstElements | SecondElements
    
    # Print intersection of both sets. Elements that are in both sets.
    # Is equivalent to FirstElements.intersection(SecondElements).
    print FirstElements & SecondElements
    
    # Print difference. Elements that are in FirstElements, but not in SecondElements.
    # Is equivalent to FirstElements.differences(SecondElements)  
    print FirstElements - SecondElements
    
    # Print symmetric difference. Elements that are either in FirstElements or SecondElements, but not in both.
    # Is equivalent to FirstElements.symmetric_difference(SecondElements).
    print FirstElements ^ SecondElements
    
    # Check if the given set is a subset of FirstElements.
    # Is equivalent to set([True, 23]).issubset(FirstElements).
    print set([True, 23]) <= FirstElements
    
    # Check if the given set is a superset of FirstElements.
    # Is equivalent to set([True, 23]).issuperset(FirstElements).
    print set([True, 23]) >= FirstElements
        
    # Remove an element form the set.
    FirstElements.remove(23)
    
    # Print set.
    print FirstElements
    
    # Pop an arbitrary element form the set.
    print FirstElements.pop()
    
    # Print set.
    print FirstElements
    
    # Remove all elements from set.
    FirstElements.clear()
    
    # Print set.
    print FirstElements
    
    # Another kind of set is the frozenset. It cannot be changed,
    # so only methods that only read the set are callable.
    FrozenElements = frozenset([1,4,6])
    
    print FrozenElements

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()