#create variable number and ask the user to input an integer
#if number is greater than or equal to 0
#    print that the number is not negative
#else
#    print that the number is negative

credit_balance = int(input('What is your credit balance? '))

if credit_balance >= 0:
    print('Your credit is not negative!.')
else:
    print('You credit is negative!.')