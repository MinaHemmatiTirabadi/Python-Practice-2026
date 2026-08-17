#Mina Hemmati

#People's names and ages are asked, then printed in dictionary format.

n=int(input("Number of people you want to include: "))
x=[]
for i in range(n):
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    x.append([name,age])
print(dict(x))
