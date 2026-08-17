#• Write a class that takes a list of names and includes the following methods:
#• Determine the name with the maximun characters
#• Determine the name with the minimum characters
class max_min:
    def __init__(self,n):
        self.n=n
        x=[]
        for i in range(n):
            a=input("Enter a name: ")
            x.append(a)
        self.x=x
        print(self.x)
        
    def mx(self):
        self.maximum=maximum
        self.maximum=self.x[0]
        for i in self.x:
            if len(i)>len(self.maximum):
                self.maximum=i
            else:
                continue
        print("-----maximum-----")
        print(f"maximum is {self.maximum}")
            
    def mn(self):
        self.minimum=minimum
        self.minimum=self.x[0]
        for i in self.x:
            if len(i)<len(self.minimum):
                self.minimum=i
                
            else:
                continue
        print("-----minimum-----")
        print(f"minimum is {self.minimum}")

minimum=0
maximum=0
n=int(input("How many names do you have?"))

p1=max_min(n)
p1.mn()
p1.mx()


            
            
