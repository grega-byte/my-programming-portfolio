# define fib(x)
#   if x == 0
#       print 'This is the base case when x = 0:', x
#       return 0
#   elif x == 1
#       print 'This is when x = 1:', x
#       return 1
#   elif x > 1
#       print 'We recall fib repeatedly here:', x
#       return fib(x-1) + fib(x-2)
#
# prompt user for input integer
#
# while number >= 0
#   print fib(number)
#   prompt user for another input integer (or negative number to stop)
# 

def fib(x):
    """Takes an input and returns the fibonacci sequence result"""
    if x == 0:
        print('This is the base case when x = 0: ', x)
        return 0
    elif x == 1:
        print('This is when x = 1: ', x)        
        return 1
    elif x > 1:
        print('We recall fib repeatedly here:', x)        
        return fib(x-1)+fib(x-2)



number = int(input('Enter a non-negative number: '))

while number >= 0:
    print(fib(number))
   
    number = int(input('Enter a non-negative number(or negative number to stop): '))