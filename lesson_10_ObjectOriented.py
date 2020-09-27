# -*- coding: cp1252 -*-
"""
File:           lesson_10_ObjectOriented.py

Description:    This script introduces object oriented description features like inheritance, properties, 
                class methods and static methods.

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
# Definitions of classes used in this demo.
#--------------------------------------------------------------------------------------------------
# Define a class vehicle as a representation for any kind of vehicles. A new-style class inherits 
# directly or indirectly from object or from a built-in type. 
class Vehicle(object):
    
    Type = "vehicle"
    
    # Initialize Vehicle class object. A class consists of attributes and methods.
    def __init__(self, Name):
        
        # The underline character defines the class element as private. It is not possible to
        # access private elements from outside the class.
        self._Name = Name
    
    # With a property it is possible to use method calls (get and set) to access an attribute.
    # The following lines show how to define a new property Name, which accesses the private
    # attribute _Name.
    def _GetName(self):
        return self._Name
    
    def _SetName(self, Name):
        self._Name = Name
        
    Name = property(_GetName, _SetName)
    
    # A normal method always has a class instance as first argument. The argument is usually called "self".    
    # Define a normal method Identify.
    def Identify(self):
        print "I am a %s with name '%s'" % (self.Type, self.Name)
    
    # A static class method doesn't have a class instance as first argument. It is possible to call a static 
    # method without an instance (see below).
    # Define a static method Drive. 
    def Drive():
        print 'I am driving anywhere'
    
    Drive = staticmethod(Drive)
    
    # A class method always has a class as it first argument. It is possible to call a class 
    # method without an instance (see below).
    # Define a class method ClassDescription. 
    def ClassDescription(cls):
        return 'This is %s class: %s' % (cls.Type, repr(cls))
    
    ClassDescription = classmethod(ClassDescription)

# Define a derived subclass Automobile, here only with single inheritance.
class Automobile(Vehicle):
    
    Type = "car"
    
    # Initialize Automobile class object.
    def __init__(self, Name, Speed):
        # Initialize super class.
        Vehicle.__init__(self, Name)
        
        # Set Speed.
        self.Speed = Speed
    
    # The property's get and set methods can be used to check the new value or to execute some code.
    def _GetName(self):
        return self._Name
    
    def _SetName(self, Name):
        if Name in ["Foo", "Bar"]:
            self._Name = Name
    
    Name = property(_GetName, _SetName)
    
    # Define a method Identify.
    def Identify(self):
        print "I am a %s with named '%s' and the maximum speed of %i mph." % (self.Type, self.Name, self.Speed)
    
    # Overwriting a base static method.
    def Drive():
        print "I am driving on streets"
    
    Drive = staticmethod(Drive)

# Define a derived subclass Train, here only with single inheritance.
class Train(Vehicle):
    
    Type = "train"
    
    # Modifying a base static method.
    def Drive():
        
        # Calling the base method.
        Vehicle.Drive()
        
        # Adding additional features.
        print "I am driving on tracks"
    
    Drive = staticmethod(Drive)

#--------------------------------------------------------------------------------------------------
# Function ExecuteLesson:
#   This function runs the lesson.
#--------------------------------------------------------------------------------------------------
def ExecuteLesson():
    
    # Constructor call of Train subclass.
    MyTrain = Train("InterCity")
    
    # Constructor call of Automobile subclass.
    MyCar = Automobile("Foo", 150)
    
    # Call a method that is inherited from base class.
    MyTrain.Identify()
    
    # Call a subclass method.
    MyTrain.Drive()
    
    # Call a method that is inherited from base class.
    MyCar.Identify()
    
    # Call a subclass method.
    MyCar.Drive()
    
    # Set the train's name.
    MyTrain.Name = "InterRegio"
    
    # Call Identify method.
    MyTrain.Identify()
    
    # Try to set a new car name. That doesn't work.
    MyCar.Name = "Baz"
    
    # Call Identify method. The old value is still set.
    MyCar.Identify()
    
    # Set the car's name again.
    MyCar.Name = "Bar"
    
    # Call Identify method. This time the new value was taken.
    MyCar.Identify()
    
    # Call class method.
    print MyCar.ClassDescription()
    
    # This works also without an instance.
    print Automobile.ClassDescription()
    
    # Also the static method Drive can be used without a class instance.
    Automobile.Drive()

# Because of the following if statement the function 'ExecuteLesson' will only be executed, if the script is started
# by itself. It won't be executed if the script is only imported.
if __name__ == "__main__":
    ExecuteLesson()
