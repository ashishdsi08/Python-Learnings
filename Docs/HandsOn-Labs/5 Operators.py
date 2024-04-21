"""
Python Operators - Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:
"""
print(10 + 5)

"""
Python divides the operators in the following groups:

Arithmetic operators  + - * % /
Assignment operators  =, +=	Ex x += 3	x = x + 3, -= x -= 3 ,x = x - 3
Comparison operators == <= >= !=
Logical operators  ( and  or not )
Identity operators - Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
x is y
x is not y
Membership operators - Membership operators are used to test if a sequence is presented in an object:
in 	-> Returns True if a sequence with the specified value is present in the object	x in y	
not in -> Returns True if a sequence with the specified value is not present in the object	x not in y
Bitwise operators -Bitwise operators are used to compare (binary) numbers:
& 	AND	Sets each bit to 1 if both bits are 1,	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1,	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1,	x ^ y	
~	NOT	Inverts all the bits,	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
"""