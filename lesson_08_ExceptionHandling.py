# -*- coding: cp1252 -*-
"""
File:           lesson_08_ExceptionHandling.py

Description:    This script introduces exception handling.

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
    
    # Catch the division by zero error.
    def Invert(Value):
        try:
            return 1.0/Value
        except ZeroDivisionError:
            print "%s has no inverse." % Value
            
    # Call the Invert function. The second call should cause an error.       
    print Invert(5.0)
    print Invert(0.0)
    
    # A second example.
    def TestFunc(Value):
        # Try to concatenate the input with an integer.
        try:
            print "Doing something with correct type of %i.\n" % Value
        # Handling a wrong input type.
        except TypeError:
            print "False parameter for TestFunc.\n"
        
    # Call the TestFunc function. The second call should cause an error.   
    TestFunc(4)
    TestFunc("ABC")
    
    # An example with two except statements.
    def PowerOfLength(InputValue, Number):
        # Try to calculate the the length of the given InputValue to the Number.
        try:
            Length = len(InputValue.keys())
            Result = Length ** Number
        # Handling a wrong input type.
        except TypeError:
            print "False parameter for function PowerOfLength."
        # Handling an attribute error.
        except AttributeError, Message:
            print "An attribute error has occurred with the following reason:\n%s" % Message
        # If no error occurs, the else statement will be executed.
        else:
            print "The result is %i." % Result
        # The finally statement will always be executed.
        finally:
            print "The function has finished.\n"
    
    # Call the TestFunc function. 
    PowerOfLength({"a" : 1, "b" : 2}, 5)
    # This function call should cause an Attribute error.    
    PowerOfLength("Test", 5)
    # This function call should cause an Type error.    
    PowerOfLength({"a" : 1, "b" : 2}, "Test")
    
    # Define an own exception.
    class InvalidNumberError(Exception):
        
        # Initialize exception.
        def __init__(self, Value):
            self.Value = Value
        
        # Define string representation.
        def __str__(self):
            return "The number %i is invalid." % self.Value
        
    # An example with a raise statement.
    def CheckInput(InputValue):
        try:
            if InputValue > 10 or InputValue < -4:
                raise InvalidNumberError(InputValue)
            
            print "Valid number: %i" % InputValue
            
        except InvalidNumberError, Message:
            print Message
            
    # Call the CheckInput function.     
    CheckInput(4)
    # This function call should cause an InvalidNumber error.  
    CheckInput(12)

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()
