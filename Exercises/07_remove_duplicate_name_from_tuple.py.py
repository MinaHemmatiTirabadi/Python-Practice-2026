#Mina Hemmati
#In the following code,
#we remove a duplicate string named "reza" from the tuple.

x=("sasan","reza","neda","omid","reza","ali","Zahra","mahan","ashkan","reza")
y=list(x)
print(y)

for i in y:
    if i=="reza":
        y.remove(i)
        

z=tuple(y)
print(z)
