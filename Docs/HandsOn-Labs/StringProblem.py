"""
Problems to Solve
1) Reverse words in a given string
input: s = “students quiz practice code” List[“students,quiz,practice,code]
Output: s = “code practice quiz students”
"""
"""
    if 
    else
        

    if 
    elif 
    elif
    elif
    
    if 
    elif 
    elif
    elif
    else
"""

def ReverseSentence(sentence):
    result = ""
    try:
        if sentence is None:
            return ""       
        
        myList = sentence.split(" ")        
        #c = myList[10000] 
        for num in range(len(myList)-1,-1,-1):
            result = result + myList[num] 

            if num != 0:
                result = result + " "        
    except:
        result ="Exception Has occured !!! Please Provide correct input"
    return result

"""
Client Code
"""
print("Hi This Is MY FIRST STRING AND FOR LOOP PROGRAM")
reversedResult = ReverseSentence("Hi This Is MY FIRST STRING AND FOR LOOP PROGRAM")
print(reversedResult)