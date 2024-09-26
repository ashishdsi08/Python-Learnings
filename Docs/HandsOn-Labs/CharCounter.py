
"""
count the number of characters in a string
INPUT : JAVAAAAAAAAAAAAAAAAAAAAAAAAAAA, A  1+1+1+1
OUTPUT : 2

INPUT : BHASKAR , K
OUTPUT : 1

INPUT : ASHISH , K
OUTPUT : 0

"""

def CharCounter(inputStr,charToCount):
    try:
        if type(inputStr) == str and type(charToCount) == str:            
            resultVal = 0
            for chr in inputStr:
                if chr ==  charToCount:
                    resultVal = resultVal +1
            return resultVal
        else:
            print("Please give proper inputs")
            return 0
    except:
        print("Exception Has Occured Check the Logs for details ")
        return 0





"""
Client Code
"""
if __name__ == "__main__":
    charCount = CharCounter(123, "KUMAR")
    print(charCount)