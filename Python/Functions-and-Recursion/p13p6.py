#define function f(x)
#   """Returns the factorial of x and prints the progress."""
#   print 'call f with x:', x 
#   if x == 0
#       print this is the initial base case
#       return 1 as 0! = 1
#   else
#       set result = x*f(x-1)
#       print 'returning', result, 'for x =', x (this shows all the returning results for x)
#       return result
#
#
#request number int input 'Enter a number'
#if number < 0 
#   print error message Error: Number entered was less than 0.
#else
#   print 'Factorial of',number,'is',f(number)
#
#

def f(x):
    """Returns the factorial of x and prints the progress."""
    print('Call f with x:', x)
    if x == 0:
        print('This is the initial base case.')
        return 1
    else:
        result = x*f(x-1)
        print('Returning', result, 'for x =',x)
        return result
       

number = int(input('Enter a number: '))

if number < 0:
    print('Error: Number entered was less than 0.')
else:
    print('Factorial of',number,'is',f(number))
    