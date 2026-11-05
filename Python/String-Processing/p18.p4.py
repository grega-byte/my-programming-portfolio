#request the first string 
#request the second string 
#
#define function f with word1 and word2 
#    change word1 to lowercase
#    change word2 to lowercase
#
#    if the last characters of word1, equal in number to the length of word2, match word2
#        return True
#    else if the last characters of word2, equal in number to the length of word1, match word1
#        return True
#    else
#        return False
#
#if calling function f with word1 and word2 returns True
#    print that one string appears at the end of the other
#else
#    print that the strings do not match at the end of each other

word1 = input('Enter your first string: ')
word2 = input('Enter your second string: ')

def f(word1,word2):
    word1 = word1.lower()
    word2 = word2.lower()

    if word1[-len(word2):] == word2:
        return True
    elif word2[-len(word1):] == word1:
        return True
    else:
        return False

if f(word1,word2) == True:
    print('One string appears at the end of the other.')
else:
    print('The strings do not match anywhere.')
