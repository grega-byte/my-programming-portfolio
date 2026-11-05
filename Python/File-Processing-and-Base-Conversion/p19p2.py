# request a string representing a number
# request an int representing the base of the number
#
# define function f with num_string and base_num as arguments
#     """Takes the number input as a string, base number 
#        and converts it to decimal."""   
#
#     reverse the number string
#     set total to 0
#
#     go through each index from 0 to the length of the number string minus 1
#         convert the digit at the current index to an int
#         multiply the digit by the base raised to the current index
#         add the result to total
#
#     return total
#
# print the original number, its base, and its decimal value

num_string = (input('Please enter a number: '))
base_num = int(input('Please enter a base >= 2 and <= 10: '))

def f(num_string,base_num):
    """Takes the number input as a string, base number and converts it to decimal."""

    rev_string = num_string[::-1]
    total = 0

    for i in range(0,len(num_string)):
        total+=int(rev_string[i])*base_num**i
    return total

print('Your number', num_string,'is',f(num_string,base_num),'from base',base_num,'to base 10.')