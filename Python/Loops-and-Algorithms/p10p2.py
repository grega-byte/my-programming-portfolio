#prompt user for input integer (0 to exit)
#
#set variable found = false
#
#while number > 0 or number < 0
#   set variable root to 0
#   for i in range 0, abs(number) plus 1
#
#       if root**3 == abs(number) and number >0
#           found = True
#           print the cube root of number is root
#       elif root**3 == abs(number) and number < 0:
#           found = True
#           print the cube root of number is (-)root 
#
#       root+=1
#
#      if found == false 
#           print number is not a perfect cube
#       set found to false
#       prompt user for input integer (0 to exit)

number = int(input('Enter a number(or 0 to exit): '))

found = False

while number > 0 or number < 0:   
    root = 0

    for i in range(0,abs(number) + 1):
        
        if root**3 == abs(number)and number > 0:
            found = True
            print('The cube root of',number,'is', str(root) +'.')
        elif root**3 == abs(number) and number < 0:
            found = True
            print('The cube root of',number,'is', str(-root) +'.')
        root+=1
    if found == False:
        print(number,'is not a perfect cube.')
    found = False
    number = int(input('Enter a number(or 0 to exit): '))