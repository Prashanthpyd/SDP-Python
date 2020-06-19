# 1. Write a python program to design simple calculator for the operators 
       # +    (addition),  
       # •  (subtraction),
       # *   (multiplication),
       # /   (division), 
       # %   (modulus), 
       # **   (exponent),  
       # //    (Floor division).

a = float(input('Enter the value of a ')) # you can also use **int(input('Enter the value of a'))**
b = float(input('Enter the value of b ')) #  and  **int(input('Enter the value of b'))**  
 # using float will help the better results in division,modulus operation

print('Addition of a and b',a+b)
print('Subtraction of a and b',a-b)
print('Multiplication of a and b',a*b)
print('Division of a and b',a/b)
print('Modulus of a and b',a%b)

print('Exponent of a and b',a**b)
#exponent of a only
print('Exponent of a only',a**a)
#exponent of b only
print('Exponent of b only',b**b)

print('Floor division of a and b',a//b)
