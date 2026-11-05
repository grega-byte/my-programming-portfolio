#define function divisors with num1 and num2 as parameters
#
#   """Find the common divisors of num1 
#   and num2. Then returns a tuple containing 
#   the common divisors of num1 num2"""
#   
#   set divisors to a tuple containing 1
#   go through each number from 2 to half of the smaller of num1 and num2
#       if num1 and num2 are both divisible by i
#           add i to divisors
#   if max num divides into min num:
#   add the smaller of num1 and num2 to divisors
#   return divisors
#
#request int enter the first number
#request int enter the second number
#
#if num1 and num2 are both greater than 1
#    print the common divisors by calling function divisors with num1 and num2
#else
#    print an error message
#

def divisors(num1,num2):
    """Find the common divisors of num1 
    and num2. Then returns a tuple containing 
    the common divisors of num1 num2"""

    divisors = (1,)
    for i in range(2, min(num1,num2)//2 + 1):

        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)
    if max(num1,num2) % min(num1,num2) == 0:
        divisors+= (min(num1,num2),)


    return divisors


num1 = int(input('Enter a number > 1: '))
num2 = int(input('Enter a number > 1: '))

if num1 > 1 and num2 > 1:
    print('The common divisors are:', divisors(num1,num2))
else:
    print('Please enter a number greater than 1.')