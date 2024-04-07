"""
Program to Check for Palindrome String
A string is said to be palindrome if the reverse of the string is the same as the string. 
For example, “abba” is a palindrome because the reverse of “abba” will be equal to “abba” 
so both of these strings are equal and are said to be a palindrome, but “abbc” is not a palindrome.

aaaabbbbbb



"""

def palindromeCheck(strToCheck):
    try:
        result = False   
        #reversedString = strToCheck[::-1]
        reversedString = ""
        for item in range(len(strToCheck)-1,-1,-1):
            reversedString = reversedString + strToCheck[item]

        if strToCheck.upper() == reversedString.upper():
            result = True        
        return result
    except:
        print("some error ocuured")

print(str.format("THE STRING IS PALINDROME Result :{}",palindromeCheck("abbA")))