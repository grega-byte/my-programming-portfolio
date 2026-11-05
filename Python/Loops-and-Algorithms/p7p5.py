#create variable total and set the total to 0
#create variable number and set it to 0
#create count variable and set it to 1
#
#while loop number < 10000
#    number += count
#    if number % 3 == 0 or number % 5 == 0
#        total += number
#
# print the total       


total = 0
number = 0

count = 1

while number < 10000:
    number += count
    if number % 3 == 0 or number % 5 == 0:
        total += number

print(total)