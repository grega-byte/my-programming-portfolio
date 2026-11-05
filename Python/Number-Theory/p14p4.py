# for number in range 2,20
#
#   set variable even_count = 0
#
#   for i in range 2,number
#       if number % i == 0
#           print number, 'equals', i, '*', number//i
#           add 1 to even_count
#
#   if even_count == 0
#       print number, 'is a prime number'
#
# print 'Finished!'




for number in range(2, 20):
    even_count = 0

    for i in range(2, number):
        if number % i == 0:
            print(number, 'equals', i, '*', number // i)
            even_count += 1

    if even_count == 0:
        print(number, 'is a prime number')

print('Finished!')