#request positive int input 
#
#def fibinacci(limit)
#   set variable a = 0
#   set variable b = 1
#   if limit ==0
#       print nothing
#   elif limit == 1
#       print 0, end =''
#   else 
#       print 0, ',', 1,sep = "", end=""
#
#       for i in range 2,limit
#           fib = b + a
#           print ',',fib, sep = "", end = ""
#           a = b
#           b = fib
#
#if limit >=0
#   fibonacci(limit)
#else
#   print error message
#

limit = int(input('Enter a non-negative number: '))

def fibonacci(limit):
    
    """Prints the first limit terms of the Fibonacci series."""
     
    a = 0
    b = 1
    
    if limit == 0:
        print()
    elif limit == 1:
        print(0,end = '')
    else:
        print(0,',',1,sep="",end = "")
        
        for i in range (2,limit): 
            fib = b+a
            print(',',fib, sep = "", end = "")
            a = b
            b = fib

if limit >= 0:
    fibonacci(limit)

else:
    print('Error. The number must be a non-negative number.')