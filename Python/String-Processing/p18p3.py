#request a sentence from the user
#
#define function code(sentence)
#    """checks a string for the word code, but the third charecter (d)
#    can be any letter upper or lower case"""
#    set count to 0
#    go through each index from 0 to the length of sentence minus 4
#        if the character at index i is 'c' and the character at index i+1 is 'o' and the lowercase character at 
#        index i+2 is in the alphabet from a to z and the character at index i+3 is 'e'
#            increase count by 1
#    return count
#
#print the number of times the pattern appears by calling function code with sentence


sentence = input('Enter a sentence: ')


def code(sentence):
    """checks a string for the word code, but the third charecter (d)
    can be any letter upper or lower case"""
    count = 0
    for i in range(0,len(sentence)-3):
       if sentence[i] == 'c' and sentence[i+1] == 'o' and sentence[i+2].lower() in 'abcdefghijklmnopqrstuvwxyz' and sentence[i+3] == 'e':
          count +=1
    return count
   
    
print('The word co_e appears',code(sentence),'times.')