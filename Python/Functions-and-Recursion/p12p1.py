#prompt user for an input int positive
#
#define fact(number) 
#   set factorial variable = 1
#   for i in range 1, number +1 
#       factorial = factorial * 1
#   return factorial 
# 
#if number >= 0
#   priunt fact(number)
#else
#   print error message
#

number = int(input('Enter a non-negative number: '))

def fact(number):
    """Returns the factorial of a non-negative int."""

    factorial = 1
    for i in range(1,number+1):
        factorial*= i
    return factorial

if number >= 0:
    print(fact(number))
else:
    print('Error! Number must be non-negative')

