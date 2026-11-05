#print how to exit
# request input int positive
#
#while number > 0
#   if number % 2 == 0 
#       print number is divisible 2
#   if number % 3 == 0 
#       print number is divisible 3
#   if number % 5 == 0 
#       print number is divisible 5
#   if number % 7 == 0  
#       print number is divisible 7
#   request input int positive
#print finished

print('Enter a negative number or 0 to exit.')
number = int(input('Please input a number:'))


while number > 0:
    if number % 2 == 0:
        print(number,'is divisible by 2.')
    if number % 3 == 0:
          print(number,'is divisible by 3.')
    if number % 5 == 0:
         print(number,'is divisible by 5.')
    if number % 7 == 0:
         print(number,'is divisible by 7.')
    number = int(input('Please input a number:'))
print('Finished!')