#input int positive (negative to exit) 
#
#while loop number > = 0
#   set variable total to 1
#   set variable count to 1
#   while count <= number
#       total*=count
#       count+=1
#   print total
#input int positive (negative to exit) 
#print finished
#

number = int(input('Enter a positive number (negative number to exit): '))


while number >= 0:
    total = 1
    count = 1
    while count <= number:
        total*=count
        count+=1
    
    print('Total positive numbers:',total)
    number = int(input('Enter a positive number (negative number to exit): '))
print('Finished!')





