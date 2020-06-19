# 9.Write a python program to swap two numbers.
# logic -- we use temp variable to hold value of 1st number
# temp = a
# a = b
# b = temp

a = int(input('Enter the value of a ')) 
b = int(input('Enter the value of b ')) 
print('------Before Swaping------')
print(a)
print(b)

temp = a
a = b
b = temp

print('------After Swaping------')
print(a)
print(b)

