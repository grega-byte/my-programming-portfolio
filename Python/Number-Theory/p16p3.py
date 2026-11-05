#define function divisors with num1 and num2 as parameters
#
#    set divisors to an empty tuple
#    go through each number from 1 to the smaller of num1 and num2
#        If num1 and num2 are both divisible by i
#            Add i to divisors
#    return divisors
#
#request int enter the first number
#request int enter the second number
#
#print the common divisors by calling function divisors with num1 and num2
#
#
def divisors(num1,num2):
    """Find the common divisors of num1 and num2 and 
    assumes that num1 and num2 are positives integers returns a table containing 
    the common divisors of num1 and num2"""

    divisors = ()
    for i in range(1, min(num1,num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)

    return divisors

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

print('The common divisors are:', divisors(num1,num2))