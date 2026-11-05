#prompt user for input non negative
#
#while limit>=0
#
#   a=0
#   b=0
#
#   if limit == 0
#       print nothing
#   elif limit == 1
#   print 0
#   else 
#       print0, ',',1,end='
#       for i in range 2,limit
#       fib = b+a
#       print ',', fib, sep'', end =''
#       a = b
#       b = fib
#
#   print new line
#   prompt user for input non negative
#print new line
#print finished



limit = int(input('Enter a non-negative integer(or negative to exit): '))
while limit >=0:
    
    a = 0
    b = 1

    if limit == 0:
        print()
    elif limit == 1:
        print(0,end = '')
    else:
        print(0,',',1,end = "")
    
        for i in range (2,limit): 
            fib = b+a
            print(',',fib, sep = "", end = "")
            a = b
            b = fib

    print()
    limit = int(input('Enter a non-negative integer(or negative to exit): '))    
print()
print('Finished!')




