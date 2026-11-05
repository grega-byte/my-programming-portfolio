# define f(x)
#   if x == 0
#       return 13
#   elif x == 1
#       return 8
#   elif x > 1
#       return f(x-2) + 13 * f(x-1)
#
# prompt user to enter a non-negative integer (>= 0)
#
# for i in range 0 to number 
#   print f(i)

def f(x):
    """Takes x and adds 13*f(x-1) with f(x-2) (uses the two previous terms)"""

    if x == 0:
        return 13
    elif x == 1:
        return 8
    elif x > 1:
        return f(x-2) + 13 * f(x-1)


number = int(input('Enter a non-negative integer (>= 0): '))

for i in range(0,number):
    print(f(i))
