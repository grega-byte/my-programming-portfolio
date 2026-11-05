#prompt user for input integer
#
#for number in range 0, number
#   set variable n = 1
#   set variable two_n = 1
#   set variable nplus1 = 1
#
#   for i in range 1, 2*number + 1
#       two_n *= i
#
#   for i in range 1, number + 2
#       nplus1 *= i
#
#   for i in range 1, number + 1
#       n *= i
#
#   print Catalan Number two_n // (nplus1 * n)
#

number = int(input('Enter a positive number: '))

for number in range(0, number):
    n = 1

    two_n = 1

    nplus1 = 1

    for i in range(1,2*number+1):
        two_n*=i

    for i in range(1,number+2):
        nplus1*=i

    for i in range(1,number+1):
        n*=i
    
    print('Catalan Number:', two_n//(nplus1*n))





