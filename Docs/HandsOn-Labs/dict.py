"""Dictionary
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

1million unique records of data ( 20 lakh employees )

1 employee if you are getting 100 updates 2-> data type will you use ?

[emplyee1 , employ2 , empl3, empl4 , 12222]

{
 1 : emplyoee1,
 2 : emplyoee2,
 3 : emplyoee3,
}

"""


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)


"""
Dictionary items are ordered, changeable, and do not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index

Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

Duplicates Not Allowed
Dictionaries cannot have two items with the same key:.

"""

print(thisdict["brand"])


"""
Duplicate values will overwrite existing values:
"""


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


"""
Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:
"""


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]

"""
there is also a method called get() that will give you the same result:"""

x = thisdict.get("model")


"""
the keys() method will return a list of all the keys in the dictionary.
"""
x = thisdict.keys()

"""
Get Values
The values() method will return a list of all the values in the dictionary.
"""


x = thisdict.values()


"""
Get Items
The items() method will return each item in a dictionary, as tuples in a list.

"""

x = thisdict.items()


"""
Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
"""


for x in thisdict:
  print(x)
  
  
for x in thisdict:
  print(thisdict[x])
  
  
for x in thisdict.values():
  print(x)
  
 
for x in thisdict.keys():
  print(x)
  
  
for x, y in thisdict.items():
  print(x, y)