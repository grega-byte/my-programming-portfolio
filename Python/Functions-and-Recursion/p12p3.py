# define function square(number, tolerance)
#   """Return an approximation of the square root of number."""
#   set count = 0
#   set step = tolerance ** 2
#   while abs(number - count squared) >= tolerance and count squared <= number
#       count = count + step
#   if abs(number - count squared) < tolerance
#       return count
#   else
#       return None
#
# set tolerance = 0.01
#
# prompt user to enter a floating-point number
#
# if number >= 0
#   print the square root of the number using square(number, tolerance)
# else
#   print error message: enter a non-negative number

def square(number, tolerance):
    """Return an approximation of the square root of number."""
    count = 0.0
    step = tolerance ** 2

    while abs(number - count ** 2) >= tolerance and count ** 2 <= number:
        count += step

    if abs(number - count ** 2) < tolerance:
        return count
    else:
        return None


tolerance = 0.01

number = float(input('Enter a floating number you want to find the square root of: '))

if number >= 0:
    print('The square root of the number', number, 'is', square(number, tolerance))
else:
    print('Error. Please enter a non-negative number.')



