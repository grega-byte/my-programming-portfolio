#request a string from the user (empty string to exit)
#
#define function tochars with word as the parameter
#    convert word to lowercase
#    set letterstring to an empty string
#    set abc to a list containing the letters a to z
#    go through each character in word
#        if the character is in abc
#            add the character to letterstring
#    return letterstring
#
#define function ispal with clean_word as the parameter
#    print that ispal was called with clean_word
#    if the length of clean_word is less than or equal to 1
#        print that true is about to be returned from the base case
#        return true
#    if the first character of clean_word is not equal to the last character
#        print that false is about to be returned because the first and last letters do not match
#        return false
#    otherwise
#        set result to the result of calling ispal with the first and last characters removed
#        print the result that is about to be returned from ispal with clean_word
#        return result
#
#while word is not an empty string
#    set clean_word to the result of calling tochars with word
#    if ispal with clean_word returns true
#        print that the string is a palindrome
#    otherwise
#        print that the string is not a palindrome
#    request another string from the user (empty string to exit)

word = input('Enter a string(empty string to exit): ')

def tochars(word):
    """makes the string lowercase and removes puntuations from the string"""
    word = word.lower()
    letterstring = ''
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in word:
        if i in abc:
            letterstring+=i
    return letterstring

def ispal(clean_word):
    """checks if the cleaned string is a palindrome"""
    print('isPal function called with argument', clean_word)

    if len(clean_word) <=1:
        print('About to return True from isPal from the base case.')
        return True
    elif clean_word[0] != clean_word[-1]:
        print('About to return False from isPal as first and last letters do not match.')
        return False
    else:
        result = ispal(clean_word[1:-1])
        print('About to return result',result, 'from isPal with argument', clean_word)
        return result 
        
while word != '':
    clean_word = tochars(word)
        
    if ispal(clean_word) == True:
        print('This is a palindrome.')
    else:
        print('This is not a palindrome.')
    word = input('Enter a string(empty string to exit): ')

