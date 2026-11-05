#import math
#create variable length and ask the user to input the length
#if length is less than 0
#    print relevant message
#else
#    calculate the area of a square
#    calculate the volume of a cube
#    calculate the area of a circle
#    calculate the volume of a sphere
#    calculate the volume of a cylinder
#    print all the results

import math

length = float(input('What is the length?'))

if length < 0:
    print('Length must be >= 0. Please try again.')
else:
    print('Area of a square:',length*length)
    print('Volume of a cube:',length**3)
    print('Area of a circle:',length**2 * math.pi)
    print('Volume of a sphere:',4/3 * math.pi * length**3)
    print('Volume of a cylinder:',math.pi * length**2 * length)