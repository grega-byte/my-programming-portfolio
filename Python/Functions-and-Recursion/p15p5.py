# define f(x)
#   if x == 0
#       print the base case
#       return 13
#   elif x == 1
#       print when x = 1
#       return 8
#   elif x > 1
#       print the recursive calculation
#       return f(x-2) + 13 * f(x-1)
#
# prompt user to enter a number >= 0 (negative number to exit)
#
# while number >= 0
#   print f(number)
#   prompt user to enter another number >= 0 (negative number to exit)

def f(x):
    """Takes x and adds 13*f(x-1) with f(x-2) (uses the two previous terms)"""

    if x == 0:
        print('This is the base case:',x)
        return 13
    elif x == 1:
        print('This is when x == 1:',x)
        return 8
    elif x > 1:
        print('Adds 13*f(x-1) with f(x-2):',x)
        return f(x-2) + 13 * f(x-1)


number = int(input('Enter a number >= 0(or negative number to exit): '))

while number >= 0:
    print(f(number))
    number = int(input('Enter a number >= 0(or negative number to exit): '))

