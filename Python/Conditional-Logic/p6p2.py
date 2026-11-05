#create variable number_1 and ask the user to input their first number
#create variable number_2 and ask the user to input their second number
#create variable number_3 and ask the user to input their third number
#create variable largest and set it to number_1
#if number_1 is even
#    if number_2 is odd
#        set largest to number_2
#    elif number_3 is odd
#        set largest to number_3
#if number_2 is odd and number_2 is greater than largest
#    set largest to number_2
#if number_3 is odd and number_3 is greater than largest
#    set largest to number_3
#if largest is odd
#    print that largest is the largest odd number
#else
#    print that none of the numbers are odd

number_1 = int(input('Please enter your first number: '))
number_2 = int(input('Please enter your second number: '))
number_3 = int(input('Please enter your third number: '))
largest = number_1

if number_1 % 2 == 0:
    if number_2 % 2 != 0:
        largest = number_2
    elif number_3 % 2 != 0:
        largest = number_3

if number_2 % 2 != 0 and number_2 > largest:
    largest = number_2

if number_3 % 2 != 0 and number_3 > largest:
    largest = number_3
if largest % 2 != 0:
    print(largest, 'is the largest odd number')   
else:
    print('None of the numbers are odd.')
    
    

