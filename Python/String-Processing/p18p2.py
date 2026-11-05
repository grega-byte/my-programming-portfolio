#request a sentence from the user
#
#define function code with word as the parameter
#    return the number of times 'code' appears in word
#
#print the number of times 'code' appears in the sentence by calling function code with word

word = input('Enter a sentence: ')


def code(word):
    """Checks how many times 'code' is in a sentence"""
    return word.count('code')    
    

print('The word code appears',(code(word)), 'times.')  
