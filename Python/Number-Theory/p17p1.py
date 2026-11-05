#define function divisors with num1 
#
#    set divisors to a tuple containing 1
#    go through each number from 2 to half of num1 + 1
#        if num1 is divisible by i
#            add i to divisors
#    add num1 to divisors
#    return divisors
#
#request an integer input greater than 1
#
#if num1 is greater than 1
#    print the divisors by calling function divisors with num1
#else
#    print an error message
#

def divisors(num1):
    """Find the common divisors of num1 
    and returns a tuple containing 
    the common divisors of num1"""

    divisors = (1,)
    for i in range(2, num1//2 + 1):

        if num1 % i == 0:
            divisors += (i,)
    divisors+= (num1,)

    return divisors

num1 = int(input('Enter a number > 1: '))

if num1 > 1:
    print('The divisors are:', divisors(num1))
else:
    print('Please enter a number greater than 1.')