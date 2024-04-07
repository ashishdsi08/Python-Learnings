#Learn about program execution in Python - Order- Functonal Programming/Scripting
#Learn about program structure
#Learn about variables in python
#Learn about global and local variables
#Learn about variable declaration syntax in python
#Learn about casting variables
#using + on variables of 2 different types
#How are variables stored in Python – Stack or Heap? (Importanat Interview Question )
#https://www.geeksforgeeks.org/how-are-variables-stored-in-python-stack-or-heap/
#https://www.prepbytes.com/blog/python/how-are-variables-stored-in-python-stack-or-heap/ 
#further read : Garbage Collection 
import CharCounter
"""
Python Variables
Variables are containers for storing data values.
Data Values -> Refernce Types or Value Types (built in data types )
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.

"""
x = 5
y = "John"
print(x)
print(y)


#Variables do not need to be declared with any particular type, and can even change type after they have been set.
z = 4        
z = "Sally"  
print(z)

"""
Casting -> What do you mean by casting?
If you want to specify the data type of a variable, this can be done with casting.
"""
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

"""
Get the Type
You can get the data type of a variable with the type() function.
"""
x = 5
y = "John"
print(type(x))
print(type(y))

"""
Single or Double Quotes?
String variables can be declared either by using single or double quotes:
"""
x = "John"
# is the same as
x = 'John'

"""
Case-Sensitive
Variable names are case-sensitive.
"""
a = 4
A = "Sally"
#A will not overwrite a


"""
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

"""
One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
"""
x = y = z = "Orange"
print(x)
print(y)
print(z)


"""
Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
"""

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

"""
Output Variables
The Python print() function is often used to output variables.
"""
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
print(x, y, z)
x = 5
y = "John"
print(x + y)

"""
Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""

localVariable = "awesome"

def myfunc():
  localVariable = "fantastic"
  print("Python is " + localVariable)
  #charCounter("","")

myfunc()

print("Python is " + localVariable)


"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""

#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""
Also, use the global keyword if you want to change a global variable inside a function.
To change the value of a global variable inside a function, refer to the variable by using the global keyword:
"""
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


"""
Quiz - Can you answer?
1)In Python, a variable must be declared before it is assigned a value: Yes/No
2)Which of the following statements assigns the value 100 to the variable x in Python:
x := 100
let x = 100
x = 100
x ← 100
x << 100
3)In Python, a variable may be assigned a value of one type, and then later assigned a value of a different type: Yes/No
4)Consider the following sequence of statements:
n = 300
m = n
Following execution of these statements, Python has created how many objects and how many references?
One object, one reference
Two objects, one reference
One object, two references
Two objects, two references
5)Which of the following are valid Python variable names:
route66
home_address
return
ver1.3
4square
Age
6)You are reading Python code, and these statements appear scattered in different locations throughout the code:

employeenumber = 4398
    .
    .
    .
EmployeeNumber = 4398
    .
    .
    .
employeeNumber = 4398

These statements refer to the same variable?
These statements refer to different variables?

7) Which of the following styles does PEP8 recommend for multi-word variable names:

distance_to_nearest_town (Snake Case)-
DistanceToNearestTown (Pascal Case)
distanceToNearestTown (Camel Case)

8) Which of the following are Python reserved words (keywords):
and
class
None
Goto
default
"""








































