#rock_paper_scissors_game with
#scissors=1
#paper=2
#rock=3

import random
count1=0
count2=0
n=1
while n<=5:
    gamer=int(input("Enter, scissors=1 or paper=2 or rock=3:"))
    print("gamer choose : ",gamer)
    if gamer<1 or gamer>3:
        print("invalid number! Try again")
        print("-------------------------")
        continue
    computer=random.randint(1,3)
    
    print("computer choose : ",computer)
    
    if gamer==1 :
        if computer==1:
            print("equal")
            count1+=0
            count2+=0
            print("-------------------------")
        elif computer==2:
            print("gamer won")
            print("-------------------------")
            count1+=1
        elif computer==3:
            print("computer won")
            print("-------------------------")
            count2+=1
    if gamer==2:
        if computer==1:
            print("computer won")
            count2+=1
            print("-------------------------")
        elif computer==2:
            print("equal")
            count1+=0
            count2+=0
            print("-------------------------")
        elif computer==3:
            print("gamer won")
            count1+=1
            print("-------------------------")
    if gamer==3:
        if computer==1:
            print("gamer won")
            count1+=1
            print("-------------------------")
        elif computer==2:
            print("computer won")
            count2+=1
            print("-------------------------")
        elif computer==3:
            print("equal")
            count1+=0
            count2+=0
            print("-------------------------")
    n=n+1
print("-----------RESULT-----------")
if count1>count2:
    print("Totally , gamer won. \n gamer score is " , count1 ,
          " and computer score is ", count2)
elif count1<count2:
    print("Totally , computer won. \n gamer score is " , count1 ,
          " and computer score is ", count2)
else:
    print("Both won.",count1)
