#Learn Python Data Types
#Learn String , int , lists , tupple , dict

"""
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
x = "Hello World"	
x = 20
x = 20.5	
x = 1j	
x = ["apple", "banana", "cherry"]	
x = ("apple", "banana", "cherry")	
x = range(6)	
x = {"name" : "John", "age" : 36}	
x = {"apple", "banana", "cherry"}	
x = frozenset({"apple", "banana", "cherry"})	
x = True , False	
x = b"Hello"	
x = bytearray(5)	
x = memoryview(bytes(5))	
x = None


"""
Python Numbers
There are three numeric types in Python:

int
float
complex
Variables of numeric types are created when you assign a value to them:
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

"""
Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:
"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""
Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
"""
import random

print(random.randrange(1, 10))


"""
Python Strings

Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:


"""

a = "Hello"
print(a)

a = """This is
a
multi line
string text"""
print(a)

a = '''This is
a
multi line
string text'''
print(a)

#Operations that can be done on strings

"""
Slicing
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

#Slice From the Start
#By leaving out the start index, the range will start at the first character:
b = "Hello, World!"
print(b[:5])

#Slice To the End
#By leaving out the end index, the range will go to the end:
b = "Hello, World!"
print(b[2:])


#Negative Indexing
#Use negative indexes to start the slice from the end of the string:
#Example
#Get the characters:

#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])

"""
Python - Modify Strings
"""

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#String Format

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



"""
Problems to Solve
1) Reverse words in a given string
input: s = “students quiz practice code” 
Output: s = “code practice quiz students”

Input: s = “i love programming very much” 
Output: s = “much very programming love i” 

2) How to Print duplicate characters from String? 

For example, if String is "Java" then the program should print "a".

3)How to check if two Strings are anagrams of each other
Two strings are anagrams if they are written using the same exact letters, ignoring space, punctuation, and capitalization.
Each letter should have the same count in both strings. For example, the Army and Mary are an anagram of each other.

4) How to find duplicate characters in a String

5) Program to Check for Palindrome String
A string is said to be palindrome if the reverse of the string is the same as the string. 
For example, “abba” is a palindrome because the reverse of “abba” will be equal to “abba” 
so both of these strings are equal and are said to be a palindrome, but “abbc” is not a palindrome.
"""
































