# define f(x)
#   if x == 1
#       print 'This is the base case:', x
#       return 2
#   elif x > 1
#       print 'This repeatedly calls x + f(x-1)', x
#       return x + f(x-1)
#
#prompt user for another input integer (0 or negative to exit)
#
# while number >= 1
#   print f(number)
#   prompt user for another input integer (0 or negative to exit)
#
def f(x):
    """Takes x and adds it with f(x-1) repeatedly till 1"""
    if x == 1:
        print('This is the base case:',x)
        return 2
    elif x > 1:
        print('This repeatedly calls x + f(x-1)',x)
        return x + f(x-1)

number = int(input('Enter a number >= 1(0 or negative to exit): '))

while number >= 1:
    print(f(number))
    number = int(input('Enter a number >= 1(0 or negative to exit): '))
