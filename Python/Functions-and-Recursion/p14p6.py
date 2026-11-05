# define fib(x)
#   if x == 0
#       return 0
#   elif x == 1
#       return 1
#   elif x > 1
#       return fib(x-1) + fib(x-2)
#
# prompt user for input integer
#
#for i in range 0,number
#    print fib(i)
# 

def fib(x):
    """Takes an input and returns the fibonacci sequence result"""
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x > 1:
        return fib(x-1)+fib(x-2)



number = int(input('Enter a non-negative number: '))


for i in range(0,number):
    print(fib(i))
   
