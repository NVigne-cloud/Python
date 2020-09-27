# -*- coding: cp1252 -*-
"""
File:           lesson_04_ControlStructures.py

Description:    This script demonstrates if and iterative control structures as loops. 

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

    # The for statement iterates over the items of any sequence (e.g. a list or a string), in the
    # order they appear in the sequence.
    
    # Iterate over a list (Output: 1 3 5).
    for Index in [1, 3, 5]:
        print Index
    
    # It is not safe to modify the sequence in the loop. It is recommended to iterate over a copy and
    # modify the original list. A list copy is created with the '[:]' operator.
    OriginalElements = [2, 4, 6]
    for Index in OriginalElements[:]:
        OriginalElements.insert(0, Index)
    
    # Print the modified list.
    print OriginalElements
    
    # The range function generates a list of arithmetic progressions (Output 0 1 2 3 4).
    print range(5)
    
    # The range function can be used to iterate over a sequence of numbers (Output: 0 1 2).
    for Index in range(0, 3):
        print Index
        
    # Define a loop with given increments (Output: 0 2 4 6).
    for Index in range(0, 8, 2):
        print Index
    
    # Define a reverse loop with given increments (Output: 8 6 4 2).
    for Index in range(8, 0, -2):
        print Index
    
    # Define a loop with index taken from mixed list (Output: 1 1.5 XYZ [5,7,8]).
    for Index in (1, 1.5, "XYZ", [5,7,8]):
        print Index
    
    # Define an if-else-statement.
    if 1 > 2:
        print "1 > 2"   
    else:
        print "1 <= 2"
    
    # Iterate over the list and print something dependent on the content.
    for Value in ["Bill", "Andy", "William"]:
        
        # Test whether a name was entered which is on the list.
        # Scopes of if- and else-branches are limited by indentation.
        if Value in ["Bill", "Henry", "Gerald"]:
            print "%s is allowed to enter!" % Value
        
        elif Value in ["Andy", "John"]:
            print "%s has to be registered!" % Value
        
        else:
            print "%s is not allowed to enter!" % Value
    
    # A for loop with a break statement.
    for Index in range(10000):
        
        # Print all even numbers.
        if Index % 2 == 0:
            print Index
        
        # Stop if the Index is over 10.
        if Index > 10:
            break  
    
    # Use the while loop.
    Index = 2
    
    # While Index is less then 10000 continue.
    while Index < 10000:
        
        print Index
        
        # Calculate Index to the power of 2.
        Index = Index ** 2
    
    # Create list of numbers.
    Numbers = range(1, 6)
    
    # Print numbers.
    print Numbers
    
    # The list comprehension provides a short way to create a new list. In the following example 
    # a new list with square numbers is created. 
    SquareNumbers = [Number * Number for Number in Numbers]
    
    # Print square numbers.
    print SquareNumbers

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()