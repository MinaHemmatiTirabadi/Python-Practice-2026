#Write code that receives a text from the user and
#filters out specific words from it.
#Mina Hemati

x=input("Enter your text: ")
x=x.upper()
y=["ARGENTINA","FOOTBALL","TEAM","MESSI","WORLD","CUP"]
for i in range(len(y)):
    x=x.replace(y[i],"*")
print(x.lower())

#Argentina’s football team has made history in the world of soccer.
#Led by the legendary Messi, the team showed great passion, skill, and
#determination during the World Cup. 
#Fans around the world celebrated Argentina’s victory and
#admired Messi’s incredible talent on the biggest football stage.
