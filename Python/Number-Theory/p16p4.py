#Define function f with limit as the parameter
#   """Prints a positive factors of the limit"""  
#Go through each number from 1 to limit
#    Set total to 0
#    Go through each number from 1 to number - 1
#        If number is divisible by i
#            Add i to total
#    If total equals number
#        Print number

#Ask the user to enter a number
#
#If limit is greater than 0
#    Call function f(limit)
#Else
#    Print an error message


def f(limit):

    """Prints a positive factors of the limit"""


    for number in range(1,limit+1):
        total = 0 

        for i in range(1,number):
            if number % i == 0:
                total +=i
        if total == number:
            print(number)
       

        
         
        
    

limit = int(input('Enter a number: '))

if limit > 0:
    f(limit)

else:
    print('Error, please use a positive integer.')