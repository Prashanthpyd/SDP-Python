# 8.Write a python program to calculate circumference of a circle.
# formula C = 2*pi*r

import math

r = int(input('Enter the radius of a Circle '))
C = 2*math.pi*r                                # with math library
print('Circumference of a Circle is',C)
#OR
print('------OR------')                        # without math library
pi = 3.1415
C = 2*pi*r
print('Circumference of a Circle is',C)
