"""
You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:

The sum of the lengths of all the words do not exceed 
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, .
The next  lines each contain a word.

Output Format

Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
Explanation

There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. 
The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" 
which corresponds to the output.You are given  words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:

The sum of the lengths of all the words do not exceed 
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, .
The next  lines each contain a word.

Output Format

Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
Explanation

There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. 
The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" 
which corresponds to the output.
"""
class UtilityCount:

    def count(words):
        uniq_words={}
        for word in words:
            if word not in uniq_words.keys():
                uniq_words[word]=1
            else:
                uniq_words[word]=uniq_words[word]+1            

        print(uniq_words.keys())
        print(uniq_words.values())
        print(uniq_words.items()) 


UtilityCount.count(["A","B","C"])


def count(words):

#    print(len(set(words)))
    uniq_words={}
    for word in words:
        if word not in uniq_words.keys():
            uniq_words[word]=1
        else:
            uniq_words[word]=uniq_words[word]+1            

    print(uniq_words.keys())
    print(uniq_words.values())
    print(uniq_words.items()) 

 

if __name__ == "__main__" :

    count(
        ['aaa','bbb','aaa','ccc','bbb','ccc','aaa']
    )