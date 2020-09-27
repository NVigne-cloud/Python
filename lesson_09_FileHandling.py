# -*- coding: cp1252 -*-
"""
File:           lesson_09_FileHandling.py

Description:    This script demonstrates the usage of file operations.

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
# The module tempfile is used to have access to the temporary system folder.
# The module codecs is used to set the encoding of files.
import tempfile
import os
import codecs

#--------------------------------------------------------------------------------------------------
# Function WriteReadTextFile:
#   This function writes and reads a text file.
#--------------------------------------------------------------------------------------------------
def WriteReadTextFile():
    # Create a file path in the temporary system folder.
    FilePath = os.path.join(tempfile.gettempdir(), "test.dat")
    
    # Open the given file for writing. Create the file if it doesn't exist.
    FileWriter = open(FilePath, 'w')
    
    # File operations should be surrounded by a try except block to be sure that the file will be closed.
    try:
        # Writes 50 lines of code into the open file consisting of line numbers.
        for Index in range(0,50):
            FileWriter.write("%i\n" % Index)
    
    except IOError:
        print "An IOError has occurred"
        
    finally:
        # Close the file handle.
        FileWriter.close()
    
    # Open a file in read-only mode and store all lines in a string list.
    FileReader = open(FilePath, 'r')
    
    # Construct two new empty lists.
    Lines1 = []
    Lines2 = []
    
    try: 
        # Read each file line.
        Line = FileReader.readline()
        
        # An endless loop terminated when the end of the file is reached.
        while Line:
            
            # Append line to list.
            Lines1.append(Line)
            
            # Read line from open file.
            Line = FileReader.readline()
        
        
        # Reposition the read pointer to start of file first.
        FileReader.seek(0)
        
        # An equivalent description - reading all lines. 
        Lines2 = FileReader.readlines()
        
    except IOError:
        print "An IOError has occurred"
        
    finally:
        # Close the file handle.
        FileReader.close()
    
    print Lines1
    print "File has %i lines of code" % len(Lines1)
    print "File has %i lines of code" % len(Lines2)

#--------------------------------------------------------------------------------------------------
# Function WriteReadUnicodeFile:
#   This function writes and reads an unicode text file.
#--------------------------------------------------------------------------------------------------
def WriteReadUnicodeFile():
    # Create unicode file.
    FilePath = os.path.join(tempfile.gettempdir(), "UnicodeText.txt")
    
    # Define unicode data.
    Data = u"This is a unicode string: 'äöüôž'."
    
    # open or create file and set unicode encoding.
    FileWriter = codecs.open(FilePath, "w", "utf-8")
    
    # Write unicode data.
    FileWriter.write(Data)
    
    # Close the file handle.
    FileWriter.close()
    
    # Try to read data without unicode encoding.
    FileReader = open(FilePath, "r")
    
    print FileReader.readline()
    
    FileReader.close()
    
    # Read data from file with unicode encoding.
    FileReader = codecs.open(FilePath, "r", "utf-8")
    
    print FileReader.readline()
    
    FileReader.close()

#--------------------------------------------------------------------------------------------------
# Function WriteReadBinaryFile:
#   This function writes and reads a binary file.
#--------------------------------------------------------------------------------------------------
def WriteReadBinaryFile():
    # Create binary file.
    FilePath = os.path.join(tempfile.gettempdir(), "TestData.bin")
    
    Data = [0, 16, 23, 35]
    
    # Write data to binary file.
    FileWriter = open(FilePath, "w")
    
    # Write the ASCII code for the given integer.
    FileWriter.write(''.join([chr(x) for x in Data]))
    
    FileWriter.close()
    
    # Read data from file.
    FileReader = open(FilePath, "rb")
    
    # Read and print the file content.
    for x in FileReader.read():
        print ord(x)
    
    FileReader.close()

#--------------------------------------------------------------------------------------------------
# Function ExecuteLesson:
#   This function runs the lesson.
#--------------------------------------------------------------------------------------------------
def ExecuteLesson():
    
    # Write and read a text file.
    WriteReadTextFile()
    
    # Write and read a unicode text file.
    WriteReadUnicodeFile()
    
    # Write and read a binary file.
    WriteReadBinaryFile()

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()