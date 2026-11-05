#create variable year and ask the user to input a year
#if year is not divisible by 4
#    print that it is a common year
#elif year is not divisible by 100
#    print that it is a leap year
#elif year is not divisible by 400
#    print that it is a common year
#else
#    print that it is a leap year

year = int(input('Please enter a year: '))

if year % 4 != 0:
    print('This year is a common year!')
elif year % 100 != 0:
    print('This is a leap year!')
elif year % 400 != 0:
    print('This year is a common year!')
else:
    print('This is a leap year!')

