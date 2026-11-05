#create variable credit_balance and ask the user to input a floating-point number
#if credit_balance is less than 0
#    print that the number is negative
#elif credit_balance is equal to 0
#    print that the number is 0
#else
#    print that the number is positive

credit_balance = float(input('What is your credit balance? '))

if credit_balance < 0:
    print('Your credit is negative! please top up.')
elif credit_balance == 0:
    print('You credit is 0! Time to top up.')
else:
    print('You credit is positive! No need to top up.')
