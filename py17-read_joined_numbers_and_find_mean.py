#We create a file with arbitrary numbers between 10 and 20.
#And then we read the file and print the average of those numbers.
#Mina Hemmati
from math import *
f1=open("a.txt","w+")
x="121517"
f1.write(x)
f1.close()

f2=open("a.txt","r")

s=f2.read(-1)
print(s)
p=0
n=""
for i in range(len(s)-1):
    if i%2==0:
        n=s[i]+s[i+1]
        m=int(n)
        p=p+m
        n=""
    else:
        continue

mean=p/(len(s)/2)
print("mean=",mean)
    





