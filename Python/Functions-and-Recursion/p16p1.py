#define function f with x as the parameter
#    if x equals 1
#        print the base case message with x
#        return 2
#    otherwise if x is greater than 1
#        print the function recall message with x
#        set result to 2 multiplied by f(x - 1)
#        print result and the value of x
#        return result
#
#request int enter an integer greater than or equal to 1 (0 or negative to exit)
#
#while number is greater than or equal to 1
#    print the result of calling function f(number)
#    request int enter an integer greater than or equal to 1 (0 or negative to exit)
#

def f(x):
    if x == 1:
        print('This is base case: ',x)
        return 2
    elif x > 1:
        print('This is recalling the function: ',x)
        result = 2*f(x-1)
        print('Returning',result, 'for when x =',x)
        return result

number = int(input('Enter an integer >=1(0 or negative to exit):'))

while number >=1:
    print(f(number))
    number = int(input('Enter an integer >=1(0 or negative to exit):'))



