#create variable age and ask the user to input an integer
#if age is less than 0
#    print relevant message
#elif age is equal to 0
#    print relevant message
#elif age is greater than 0 and less than or equal to 20
#    print relevant message
#elif age is greater than 20 and less than or equal to 40
#    print relevant message
#elif age is greater than 40 and less than or equal to 60
#    print relevant message
#elif age is greater than 60 and less than or equal to 80
#    print relevant message
#elif age is greater than 80 and less than or equal to 100
#    print relevant message
#else
#    print that the number is greater than 100

age = int(input('What age are you? '))

if age<=0:
    print('Time to grow!')
elif 0<age<=20:
    print('You are still only young!')
elif 20<age<=40:
    print('You are in your learning years.')
elif 40<age<=60:
    print('How are the kids?')
elif 60<age<=80:
    print('Enjoy retirement.')
elif 80<age<=100:
    print('You have come a long way..')
else:
    print('You are old and wise!')
