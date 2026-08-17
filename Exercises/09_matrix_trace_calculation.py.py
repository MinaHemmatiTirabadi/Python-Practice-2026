#Write code that accepts a matrix from the user and
#prints the sum of the original diagonal elements.
#Mina Hemmati
n=int(input("Enter the number of rows of the desired matrix."))
x=[]
for i in range(n):
    y=[]
    for j in range(n):
        print("You are in row ",i," and column ",j," of the matrix.")
        a=float(input("The element of Matrix: "))
        y.append(a)
    x.append(y)
for r in x:
    print(r)
c=0
for i in range(n):
     c=c+x[i][i]
print("The trace is equal to ",c)
    
