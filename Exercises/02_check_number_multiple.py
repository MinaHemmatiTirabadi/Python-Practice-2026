#Is the number n a multiple of the number m?
#Mina Hemmati
def num(n,m):
    if n%m==0:
        print(n," is a multiple of ",m)
    else:
        print(n," is not a multiple of ",m)

n=int(input("Enter your first number : "))
m=int(input("Enter your second number : "))
num(n,m)
