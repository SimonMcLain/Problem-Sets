# Simon McLain 2018-03-30
"""Write a function sumultiply that takes two integer arguments and returns their
product. The function should not use the * or / operators. For example:
> sumultiply(11, 13)
143
> sumultiply(5, 123)
615"""


a = int(input("Enter a positive integer for the first factor to be multiplied: ")) 
b = int(input("Enter a positive integer for the second factor to be multiplied: "))

def sumultiply(a, b):
  total = 0
  for i in range(0, b):
    total = total + b 
  return total

print("The product of these two factors is: ", sumultiply(a, b))

