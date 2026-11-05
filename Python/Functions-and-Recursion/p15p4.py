# define f(x)
#   if x == 1
#       return 1
#   elif x > 1
#       return f(x-1) + 2**(x-1)
#
# prompt user to enter a positive integer (>=1)
#
# for i in range 1, number + 1
#   print f(i)

def f(x):
    """This function adds 2**(x - 1) with the previous function result"""
    if x == 1:
        return 1
    elif x > 1:
        return f(x-1) + 2**(x-1)


number = int(input('Enter a number >= 1: '))

for i in range(1,number+1):
    print(f(i))