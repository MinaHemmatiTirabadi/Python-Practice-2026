#tree
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    def n(self):
        node=self
        score=0
        
        while node!=None:
            print(node.val)
            a1=input("answer the q with t / T / f / F : ")
            if a1=="t" or a1=="T":
                node=node.left
                score=score+1
                print("score: ",score)
                print("---------------")
            elif a1=="f" or a1=="F":
                node=node.right
                print("score: ",score)
                print("-------finish--------")
            if node==None:
                print("-------finish--------")
            
                
            
            
        
q1="money > science?"
q2="money > power?"
q3="power > science?"
q4="health > power?"
q5="health > money?"
q6="health > science?"



node1=Node(q1)
node2=Node(q2)
node3=Node(q3)
node4=Node(q4)
node5=Node(q5)
node6=Node(q6)


node1.left=node2
node1.right=node3

node2.left=node4
node2.right=node5

node4.left=node5
node4.right=node6

node5.left=node6


node1.n()

      
