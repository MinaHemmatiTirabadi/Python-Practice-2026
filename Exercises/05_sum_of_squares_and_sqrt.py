#Fifth session
#Mina Hemmati

#Receives the number n from the user and 
#calculates the sum of the squares of the numbers 1 to n and
#the square root of the result.

import math as m
n=int(input("n="))
s=0
for i in range(n+1):
    i=m.pow(i,2)
    s=s+i
print("Sum=",s)
q=m.sqrt(s)
print("The square root of the result is",q)
