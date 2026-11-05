#   request input integer 
#
#if number < 0
#   print error message
#else
#   fact = 1
#   i=1
#   whilei<=number
#       fact*=i
#       i+=1
#   print factorial of number is fact
#

number = int(input('Enter a number: '))



if number < 0:
    print('Error: Number entered was less than 0.')
else:
    fact = 1 
    i = 1
    while i <= number:
        fact*=i
        i+=1
    print('Factorial of',number,'is',fact)









