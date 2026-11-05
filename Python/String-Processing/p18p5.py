#request a string
#
#define function xyz with sentence
#    go through each index from 0 to the length of sentence minus 2
#        if the character at index i is 'x' and the character at index i+1 is 'y' and the character at index i+2 is 'z'
#            if index i is 0 or the character at index i-1 is not a full stop
#                return True
#    return False
#
#print(xyz(sentence))


sentence = input('Enter a string: ')


def xyz(sentence):
    """checks a string for xyz, but the charecter before xyz must not be a '.'"""

    for i in range(0,len(sentence)-2):
       if sentence[i] == 'x' and sentence[i+1] == 'y' and sentence[i+2] == 'z':
          if i == 0 or sentence[i-1] != '.':
            return True
    return False
          
            
print(xyz(sentence))