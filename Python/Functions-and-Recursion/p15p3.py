# define f(x)
#   if x == 1
#       print 'This is the base case:', x
#       return 1
#   elif x > 1
#       print 'We recall f(x) here:', x
#       return f(x-1) + 2**(x-1)
#
# prompt user to enter an integer >= 1 (0 or negative to exit)
#
# while number >= 1
#   print f(number)
#   prompt user to enter another integer >= 1 (0 or negative to exit)

def f(x):
    """This function adds 2**(x - 1) with the previous function result"""
    if x == 1:
        print('This is the base case:',x)
        return 1
    elif x > 1:
        print('We recall f(x) here:',x)
        return f(x-1) + 2**(x-1)

number = int(input('Enter a number >= 1(0 or negative to exit): '))

while number >= 1:
    print(f(number))
    number = int(input('Enter a number >= 1(0 or negative to exit): '))
   