# define f(x)
#   if x == 1
#       return 2
#   elif x > 1
#       return x + f(x-1)
#
# prompt user for input integer
# convert number to integer
#
# for i in range 1, number + 1
#   print f(i)
#

def f(x):
    """Takes x and adds it with f(x-1) repeatedly till 1"""
    if x == 1:
        return 2
    elif x > 1:
        return x + f(x-1)


number = int(input('Enter a number >=1: '))

for i in range(1,number+1):
    print(f(i))