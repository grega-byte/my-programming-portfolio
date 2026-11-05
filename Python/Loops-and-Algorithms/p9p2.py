#   request input int positive (or negative to exit)
#
#while number greater than 0
#   create variable total = 0
#   for i in range 1, number +1
#       total+=1
#   print total
#   request input int positive (or negative to exit)
#print total
#print finished 


number = int(input('Enter a positive number(negative number to exit: '))

while number>0:
    total = 0
    for i in range(1,number+1):
        total+=i
    print('Total positive numbers:',total)
    number = int(input('Enter a positive number(negative number to exit: '))
    

print('Finished!')



