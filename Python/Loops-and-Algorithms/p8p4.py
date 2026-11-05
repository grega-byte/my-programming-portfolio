#print statement how to exit
#request number to input int positive
#
#set variable range_0=0
#set variable range_1=0
#set variable range_2=0
#set variable range_3=0
#set variable range_4=0
#set variable range_5=0
#set variable range_6=0
#
#set while number >=0
#   if number == 0
#       print number equal to 0
#       range_0 +=1
#   elif number == 0
#       print number equal to 0
#       range_0 +=1
#   elif number > 0 and number <= 20:
#       print number > 0 and <= 20
#       range_1+=1
#   elif number > 20 and number <= 40:
#       print number > 20 and <= 40
#       range_2+=1
#   elif number > 40 and number <= 60:
#       print number > 40 and <= 60
#       range_3+=1    
#   elif number > 60 and number <= 80:
#       print number > 60 and <=80
#       range_4+=1
#   elif number > 80 and number <= 100:
#       print number > 80 and <=100
#       range_5+=1
#   elif number > 100:
#       print Number is greater than 100
#       range_6+=1
#   request number to input int positive
#
#print new line
#print Finished!
#print new line
#print Range 0: range_0
#print Range 0 - 20: range_1
#print Range 20 - 40: range_2
#print Range 40 - 60: range_3)
#print Range 60 - 80: range_4)
#print Range 80 - 100: range_5)
#print Range > 100: range_6)
#print new line



print('Enter a number less than 0 to exit.')
number = int(input('Please enter a positive number: '))

range_0 = 0
range_1 = 0
range_2 = 0
range_3 = 0
range_4 = 0
range_5 = 0
range_6 = 0


while number >=0:
    if number == 0:
        print('Number is equal to 0')
        range_0+=1
    elif number > 0 and number <=20:
        print('Number is greater than 0 and less than or equal to 20')
        range_1+=1
    elif number > 20 and number <=40:
        print('Number is greater than 20 and less than or equal to 40')
        range_2+=1
    elif number >40 and number <= 60:
        print('Number is greater than 40 and less than or equal to 60')
        range_3+=1    
    elif number > 60 and number <= 80:
        print('Number is greater than 60 and less than or equal to 80')
        range_4+=1
    elif number > 80 and number <= 100:
        print('Number is greater than 80 and less than or equal to 100')
        range_5+=1
    elif number > 100:
        print('Number is greater than 100')
        range_6+=1
    number = int(input('Please enter a positive number: '))
print()
print('Finished!')
print()
print('Range 0:', range_0)
print('Range 0 - 20:',range_1)
print('Range 20 - 40:',range_2)
print('Range 40 - 60:',range_3)
print('Range 60 - 80:',range_4)
print('Range 80 - 100:',range_5)
print('Range > 100: ',range_6)
print()





    