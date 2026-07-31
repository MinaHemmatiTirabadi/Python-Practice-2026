#A project has three phases.
#Given the best and worst completion times for each phase,
#write code that estimates the project completion time for
#a Gaussian distribution function.

################################################
import random
from math import sqrt
def mu(a,b):
    return (a+b)/2
def sigma(a,b,mu):
    return sqrt(0.5*(a-mu)**2+0.5*(b-mu)**2)

p1a=7
p1b=15
p2a=20
p2b=48
p3a=23
p3b=60
n=1000
s1=0
s2=0
s3=0

for i in range(n):
    a=p1a
    b=p1b
    m=mu(a,b)
    s=sigma(a,b,m)
    p1=random.gauss(m,s)
    s1=s1+p1

    a=p2a
    b=p2b
    m=mu(a,b)
    s=sigma(a,b,m)
    p2=random.gauss(m,s)
    s2=s2+p2

    a=p3a
    b=p3b
    m=mu(a,b)
    s=sigma(a,b,m)
    p3=random.gauss(m,s)
    s3=s3+p3

mp1=s1/n
mp2=s2/n
mp3=s3/n
total=mp1+mp2+mp3
print("p1=",mp1)
print("p2=",mp2)
print("p3=",mp3)
print("total=",total)
    















    

    
