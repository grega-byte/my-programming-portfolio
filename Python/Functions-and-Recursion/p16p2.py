#define function f with x as the parameter
#    if x equals 1
#        return 2
#    otherwise if x is greater than 1
#        return 2 multiplied by f(x - 1)
#
#request int enter an integer greater than or equal to 1 (0 or negative to exit)
#
#while number is greater than or equal to 1
#    go through each number from 1 to number
#        print f(i)
#    request int enter an integer greater than or equal to 1 (0 or negative to exit)
#

def f(x):
    if x == 1:
        return 2
    elif x > 1:
        return 2*f(x-1)
         

number = int(input('Enter an integer >=1(0 or negative to exit):'))

while number >=1:
    for i in range(1,number+1):
        print(f(i))
    number = int(input('Enter an integer >=1(0 or negative to exit):'))


