#Finds the distance between two coordinate points.
#Mina Hemmati
import math as m
def distance(x_1,y_1,x_2,y_2):
    d=m.sqrt(m.pow((x_2-x_1),2)+m.pow((y_2-y_1),2))
    print("The distance between two given points is equal to",d)
    
    


print("Enter the first coordinate information:")
x_1=float(input("Enter the point width: "))
y_1=float(input("Enter the length of the point: "))
print("------------------------------------------")
print("Enter the second coordinate information:")
x_2=float(input("Enter the point width: "))
y_2=float(input("Enter the length of the point: "))
print("------------------------------------------")
distance(x_1,y_1,x_2,y_2)
