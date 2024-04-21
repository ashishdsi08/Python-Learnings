word = "aaaaaswsASWWEORKRdewfefv"

def _reverse_case(wordtoreverse):

    result = ""

    for word in wordtoreverse:

        if word.islower():

           result = result + word.upper()

        else:

            result = result + word.lower()

        

    print ("Print this Result",result) 

        

_reverse_case (word)