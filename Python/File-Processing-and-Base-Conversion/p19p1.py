# request a number in base 10
# request a base between 2 and 10
#
# define function base with base_ten and base_num
#     set cal to an empty string
#
#     if base_num is less than 2 or greater than 10
#         return 'invalid'
#
#     if base_ten equals 0
#         return '0'
#
#     while base_ten is greater than 0 and base_num is between 2 and 10
#         find the remainder when base_ten is divided by base_num
#         convert the remainder to a string and add it to cal
#         divide base_ten by base_num using integer division
#
#     reverse cal and return it
#
# print the original base 10 number, its converted value, and the new base

base_ten = int(input('Please enter a number in base 10: '))
base_num = int(input('Please enter a base >= 2 and <= 10: '))


def base(base_ten,base_num):
    """checks a decimal number and changes it into the base numbers format."""
    cal = ''
    if base_ten < 0 or base_num < 2 or base_num > 10:
        return 'invalid'
    if base_ten == 0:
        return '0'

    while base_ten > 0:


        remainder = base_ten % base_num
        cal+= str(remainder)
        base_ten = base_ten//base_num 
    return cal[::-1]
print('Your base 10 number',base_ten,'is number',base(base_ten,base_num),'in base',base_num)        

 