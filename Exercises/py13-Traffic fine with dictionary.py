#Mina Hemmati

#Write a program to issue a car violation ticket.
#• The total number of different types is 10
#• Consider the fine for each different type differently.
#• In your code, the program should print the total fine
#from the number and type of codes.

dic={"a1":100000,"a2":50000,"a3":250000,"a4":410000,"a5":360000,
     "a6":950000,"a7":450000,"a8":520000,"a9":670000,"a10":83000}
f1=open("py13Exe.txt","w+")
fname=input("first name: ")
lname=input("last name: ")
r1=fname+" "+lname+"\n"
f1.write(r1)
r2="---------------\n"
f1.write(r2)
n=int(input("Please enter the number of violations: "))

listkeys=[]
s=0
while n>=1:
    v=input("type of violation:[a1,...,a10] ")
    listkeys=dic.keys()
    if v not in listkeys:
        print("enter correct name")
    else:
        nv=int(input("How many ?"))
        if nv<=n: 
            n=n-nv
            print("n=",n)
            s=s+(dic[v]*nv)
            r3=v+" * "+str(nv)+" = "+str(dic[v]*nv)+"\n"
            f1.write(r3)
        else:
            print("try again")
r4="---------------\n"
f1.write(r4)
r6="fine = "+str(s)+"\n"
f1.write(r6)
f1.close

        
