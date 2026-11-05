#prompt user for input integer (negative to exit)
#
#set variable found = false
#
#while number >= 0
#   set variable root to 0
#   for i in range 0, number plus 1
#       if root**2 == number 
#           found = True
#           print the square root of number is root
#       root+=1
#      if found == false 
#           print number is not a perfect square
#       set found to false
#       prompt user for input integer (negative to exit)

number = int(input('Enter a positive number(or negative number to exit): '))

found = False

while number >=0:   
    root = 0
    for i in range(0,number+1):
        
        if root**2 == number:
            found = True
            print('The square root of',number,'is', str(root) +'.')
        root+=1
    if found == False:
        print(number,'is not a perfect square.')
    found = False
    number = int(input('Enter a number(or negative number to exit): '))