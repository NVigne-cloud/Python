# -*- coding: cp1252 -*-
"""
File:           lesson_07_ArgumentHandling.py

Description:    This script demonstrates the definition of functions and the different types of argument passing.

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
    
    # Example for a function without arguments.
    def PrintMyFunc():
        print 'MyFunc'
    
    # Call function.
    PrintMyFunc()
    
    # Example for a function with one argument.
    def CalculatePowerOf2(Value):
        # Calculate and return the power of 2 for the given value.
        return Value ** 2
    
    # Call function.
    print CalculatePowerOf2(3)
    
    # Function with defaulted arguments.
    def FunctionWithDefaultedArguments(a = 1, b = "Hallo"):
        print "%s, %s" % (a, b)
    
    # Different calls of the function with defaulted arguments.
    FunctionWithDefaultedArguments(0)
    FunctionWithDefaultedArguments(9, 2)
    FunctionWithDefaultedArguments(b = 7)
    
    # Function with variable arguments.
    def FunctionWithVariableArguments(*VariableArgs):
        # If arguments are given, iterate over them.
        if VariableArgs:
            
            print "%i argument(s) given:" % len(VariableArgs)
            
            # Print each element and it's type.
            for Argument in VariableArgs:
                print "Argument %s of type %s" % (Argument, type(Argument))
        else:
            print "No arguments given"
        
        # Print a blank line.
        print 
    
    # Different calls of the function with variable arguments.
    FunctionWithVariableArguments()
    FunctionWithVariableArguments(1, "Hello")
    FunctionWithVariableArguments(True)
    
    # Call with arguments given in a variable
    ArgumentTuple = (1,2,3)
    FunctionWithVariableArguments(*ArgumentTuple)
    
    # Function with variable arguments.
    def FunctionKeywordArguments(**KeyWordArgs):
        
        # Sort the keywords.
        Keys = KeyWordArgs.keys()
        Keys.sort()
        
        # Iterate over the keywords.
        for Key in Keys:
            # Print the key value pairs.
            print "%s : %s" % (Key, KeyWordArgs[Key])
        
        # Check if the keyword "Test" is given.
        if "Test" in Keys:
            print "'Test' keyword found!"
        
        else:
            print "'Test' keyword not found!"
        
        # Print a blank line.
        print 
    
    # Different calls of the function with variable keywords.
    FunctionKeywordArguments()
    FunctionKeywordArguments(Test = 1, Test2 = 2)
    FunctionKeywordArguments(Key1 = 2, Key2 = 4, Key3 = 6, Key4 = 1)
    
    # Call with arguments given in a variable
    ArgumentDictionary = dict(KeyA=1, KeyB=2, KeyC=3)
    FunctionKeywordArguments(**ArgumentDictionary)
    
    # Function different kinds of arguments.
    def FunctionWithDifferentArguments(a, b = None, *VariableArgs, **KeyWordArgs):
        
        # Print a and b, if b is given. Otherwise print only a.
        if b is None:
            print "a = %s" % a
        else:
            print "a, b = %s, %s" % (a, b)
        
        if VariableArgs:
            print "Args: " + str(VariableArgs)
        
        if KeyWordArgs:
            print "Keywords: %s" % KeyWordArgs
        
        # Print a blank line.
        print 
    
     # Different calls of the function with different kinds of parameters.
    FunctionWithDifferentArguments(3, k = "Hello")
    FunctionWithDifferentArguments(3, 2, 15, 12, c = 3)

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()