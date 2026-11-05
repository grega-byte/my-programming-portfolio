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
#set clean_word to the result of calling tochars with word
#set letter to 0
#set reverse to the length of clean_word minus 1
#set ispal to true
#
#while letter is less than or equal to reverse
#    if the character at position letter in clean_word is not equal to the character at position reverse in clean_word
#        set ispal to false
#        stop the loop
#    else
#        increase letter by 1
#        decrease reverse by 1
#
#if ispal is true
#    print that the string is a palindrome
#else
#    print that the string is not a palindrome

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

clean_word = tochars(word)
letter = 0
reverse = len(clean_word)-1
ispal = True 

while letter <= reverse:
    
    if clean_word[letter] != clean_word[reverse]:
        ispal = False
        break
    else:
        letter+=1
        reverse-=1

if ispal == True:
    print('This is a palindrome.')
else:
    print('This is not a palindrome.')

