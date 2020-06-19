# 3.Write a python program to calculate area of a circle.
# formula A = (pi*(r**2))
# import math library for constant values and mathematical functions

import math

r = int(input('Enter the radius of a Circle '))
A = (math.pi*(r**2))                            # with math library
print('Area of Circle is',A)
 # OR
print('------OR------')                         # without math library
pi = 3.1415
A1 = (pi*(r**2))
print('Area of Circle is',A1)