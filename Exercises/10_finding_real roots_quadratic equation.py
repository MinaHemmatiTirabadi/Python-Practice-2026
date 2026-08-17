# Finding the real roots of a quadratic equation
#Mina Hemmati
import math as m
print("Suppose the quadratic equation is in the form ax\u00B2+bx+c .")
a=float(input("Enter the coefficient of the term x\u00B2 : "))
b=float(input("Enter the coefficient of the term x\u00B1 : "))
c=float(input("Enter the coefficient of the term x\u00B0 : "))
delta=m.pow(b,2)-4*a*c
if delta>0:
    x_1=((-1*b)+m.sqrt(delta))/(2*a)
    x_2=((-1*b)+(-1)*(m.sqrt(delta)))/(2*a)
    print("The first real root is equal to ",x_1)
    print("The second real root is equal to ",x_2)
elif delta==0:
    x=(-1*b)/2*a
    print("The equation has a single root ",x)
elif delta<0:#else:print("donot have roots")
    print("The equation has no real roots.")
