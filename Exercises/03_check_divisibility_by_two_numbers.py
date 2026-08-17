#Is the number n divisible by both p and q?
#Mina Hemmati
def num(n,x):
    if n%x==0:
        print(n," is a multiple of ",p," and ",q)
    else:
        print(n," is not a multiple of ",p," and ",q)

n=int(input("Enter your integer : "))
p=int(input("Enter p : "))
q=int(input("Enter q : "))
x=p*q
num(n,x)
