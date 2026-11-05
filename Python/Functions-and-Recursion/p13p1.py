#define function max a,b 
#   """ Function that returns the largest of its two arguments"""
#   if a > b:
#       return a
#   else
#       return b
#request number_1 input float 'Enter a number'
#request number_2 input float 'Enter a number'
#set variable biggest = max(number_1,number_2)
#
#print The largest of', number_1,'and', number_2,'is', biggest
#

def max(a,b):
    """ Function that returns the largest of its two arguments"""

    if a>b:
        return a
    else:
        return b 

number_1 = float(input('Enter a number: '))
number_2 = float(input('Enter a number: '))

biggest = max(number_1,number_2)

print('The largest of', number_1,'and', number_2,'is', biggest)