# -*- coding: cp1252 -*-
"""
File:           lesson_01_StringHandling.py

Description:    This script demonstrates elementary and advanced features of string handling. This includes
                string concatenation, type converting and string modifying.

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
# Function BasicStringHandling:
#   This shows some basic string handling features.
#--------------------------------------------------------------------------------------------------
def BasicStringHandling():

    # A first ASCII string object.
    AsciiText = "ASCII"
    
    # An unicode string object with default encoding.
    UnicodeTextWithDefaultEncoding = u"Unicode"
    
    # An unicode string object with given latin encoding.
    UnicodeTextWithGivenEncoding = unicode("Unicode encoded", "cp1252")
    
    # String concatenation.
    ConcatenatedText = AsciiText + UnicodeTextWithDefaultEncoding
    
    # Output on standard IO.
    print ConcatenatedText
    
    # Create one string out of a list. The elements are concatenated with the join function and
    # a blank is inserted between two elements.
    JoinedText = " ".join([AsciiText, UnicodeTextWithDefaultEncoding, UnicodeTextWithGivenEncoding])
    
    # Output on standard IO.
    print JoinedText

    # The % operator can be used for string formatting. 
    print "This is a string: '%s'" % AsciiText
    
    # Output, masking and string conversion of an integer variable (in this case the length of a string).
    # If '%i' is used, only integer values are accepted.
    print "The length of \"ConcatenatedText\" is: %i" % len(ConcatenatedText)
    
    # Convert to an integer representing the unicode code point of the character.
    print ord("a")
    
    # Reconverting the integer to string.
    print chr(ord("a"))
    
    # Reconverting the integer to unicode string.
    print unichr(ord("a"))

#--------------------------------------------------------------------------------------------------
# Function TypeConverting:
#   This shows how to convert string to other types.
#--------------------------------------------------------------------------------------------------
def TypeConverting():
    # Declare a string variable denoting a float.
    FloatText = "1.01234"   
    # Print its type.
    print type(FloatText)    
    
    # Declare a string variable denoting an integer.
    IntegerText = "12345"   
    # Print its type.
    print type(IntegerText)
    
    # Convert the first string to float.
    FloatTextToFloat = float(FloatText)
    # Print its type. 
    print type(FloatTextToFloat)
    
    # Reconvert the float to string using repr.
    ReprFloat = repr(FloatTextToFloat)
    # Print its type.
    print type(ReprFloat)
    
    # Convert the second string to integer.
    IntegerTextToInteger = int(IntegerText)     
    # Print its type.
    print type(IntegerTextToInteger)
    
    # Reconvert the integer to string using repr.
    ReprInteger = repr(IntegerTextToInteger)
    # Print its type.
    print type(ReprInteger)

#--------------------------------------------------------------------------------------------------
# Function AdvancedStringHandling:
#   This shows some advanced string handling features.
#--------------------------------------------------------------------------------------------------
def AdvancedStringHandling():
    
    # Example of a protocol string.
    Protocol = "TRUE##5#1.0#2.0#3.0#4.0#5.0#"
    
    # Split the regular build string into a component list.
    ProtocolElements = Protocol.split("#")
    # Print the protocol list.
    print ProtocolElements
    
    # Declare a new string.
    NewText = " This is a string!   "

    # Show original text 
    print "'%s'" % NewText
    
    # Delete leading and trailing whitespace.
    print "'%s'" % NewText.strip()
    
    # Delete leading whitespace.
    print "'%s'" % NewText.lstrip()
    
    # Delete trailing whitespace.
    print "'%s'" % NewText.rstrip()
    
    # Convert the string to lowercase.
    print "'%s'" % NewText.lower()
    
    # Convert the string to uppercase.
    print "'%s'" % NewText.upper()
    
    # Replace all 'i's with 'k's.
    print "'%s'" % NewText.replace("i", "k")
    
    # Find first occurrences of "s".
    print NewText.find("s")

#--------------------------------------------------------------------------------------------------
# Function ExecuteLesson:
#   This function runs the lesson.
#--------------------------------------------------------------------------------------------------
def ExecuteLesson():
   
    # Execute basic string handling features.
    BasicStringHandling()
    
    # Execute string type converting features.
    TypeConverting()
    
    # Executes some advanced string handling features.
    AdvancedStringHandling()

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()