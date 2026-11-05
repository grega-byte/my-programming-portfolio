#create variable year and ask the user to input a year
#if year is divisible by 4 and year is not divisible by 100 or year is divisible by 400
#    print that it is a leap year
#
#else
#    print that it is a common year

year = int(input('Please enter a year: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('This is a leap year!')
else:
    print('This year is a common year!')
    

