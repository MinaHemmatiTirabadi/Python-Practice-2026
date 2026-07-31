#We ask the user for their name, national ID number, and phone number.
#And we ask them to create a password.
#The code checks that the password does not include
#their full name, full ID number, or full phone number.

#Mina Hemmati
import re
n=input("Enter your first name: ")
words = n.split()
ID=input("Enter your id number: ")
phone=input("Enter your phone number: ")
pas=input("Choose a password, please: ")
x=True
while x:
    for i in range(len(words)-1):
        if not re.search(words[i],pas):
            break
  
    if not re.search(ID,pas):
        break
    elif not re.search(phone,pas):
        break
    else:
        print("Valid Password.")
        x=False
        break
if x:
    print("invalid password. try again.")
    
        

