#number = 100
#
#define function f(x)
#   """Function that adds 1 to its argument and prints it out"""
#   set number = 10
#
#   print('In function f:')
#   x += 1
#   y = 1
#   print 'x is', x
#   print 'y is', y
#   print 'z is', z
#   print 'Number is', number
#
#   return x + number
#
#x, y, z = 5, 10, 15
#
#print('Before function f:')
#print('x is', x)
#print('y is', y)
#print('z is', z)
#print number
#
#z = f(x)
#
#print('After function f:')
#print('x is', x)
#print('y is', y)
#print('z is', z)
#print number
#
#

number = 100

def f(x):
    """Function that adds 1 to its argument and prints it out"""
    number = 10

    print('In function f:')
    x+=1
    y=1
    print('x is', x)
    print('y is', y)
    print('z is', z)
    print('Number is', number)
    return x + number

x,y,z = 5,10,15


print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print(number)
print()
z = f(x)
print()
print('After function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print(number)
print()
