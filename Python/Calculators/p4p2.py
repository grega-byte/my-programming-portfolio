import math

length = float(input('What is the length?'))

print('Area of a square:',length*length)
print('Volume of a cube:',length**3)
print('Area of a circle:',length**2 * math.pi)
print('Volume of a sphere:',4/3 * math.pi * length**3)
print('Volume of a cylinder:',math.pi * length**2 * length)