# -*- coding: cp1252 -*-
"""
File:           lesson_06_DictionaryHandling.py

Description:    This script demonstrates the definition of dictionaries and the usage of the 
                predefined operators and methods.

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
    
    # Creation of a new dictionary. Equivalent to TelephoneNumbers = dict(Jim=54, John=12, Jake=58).
    TelephoneNumbers = {"Jim": 54, "John": 12, "Jake": 58}
    
    # Adding a new entry.
    TelephoneNumbers["Frank"] = 40
    
    # Testing for keys.
    print TelephoneNumbers["Jake"]
    
    # Print all available keys and the associated numbers.
    for Name, Number in TelephoneNumbers.items():
        print "%s at phone %i" % (Name, Number)
    
    Names = ["Jim", "Tim", "John"]
    
    for CurrentName in Names:
        # Test if NewName is a key in the dictionary.
        if CurrentName in TelephoneNumbers:
            print "%s at phone %i." % (CurrentName, TelephoneNumbers[CurrentName])
        else:
            print "%s not found in dictionary!" % CurrentName
    
    # Get the list of keys.
    NamesInDictionary = TelephoneNumbers.keys()
    
    # Print list.
    print NamesInDictionary
    
    # Get the list of values.
    NumbersInDictionary = TelephoneNumbers.values()
    
    # Print list.
    print NumbersInDictionary
    
    # Get the number of entries.
    print "The list has %i entries." % len(TelephoneNumbers)
    
    # Update dictionary with the content of second dictionary.
    TelephoneNumbers.update({"Jim": 33, "Jane" : 99})
    
    # Print dictionary.
    print TelephoneNumbers
    
    # Create a copy of the dictionary.
    CopyOfTelephoneNumbers = TelephoneNumbers.copy()
    
    # Create only a reference
    NoCopyOfTelephoneNumbers = TelephoneNumbers
    
    # Change value of original dictionary.
    TelephoneNumbers["Frank"] = 89
    
    # Print dictionary.
    print TelephoneNumbers
    
    # Print copy of dictionary.
    print CopyOfTelephoneNumbers
    
    # Print reference of dictionary.
    print NoCopyOfTelephoneNumbers
    
    # Set default. If the key is in the dictionary, return it's value. If not, insert key with the given 
    # default value an return the value.
    print TelephoneNumbers.setdefault("Jacob", 17)
    
    print TelephoneNumbers.setdefault("Jane", 14)
    
    print TelephoneNumbers.setdefault("William")
    
    # Print dictionary.
    print TelephoneNumbers

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()