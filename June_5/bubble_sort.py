class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next is not None:
                    print(temp.data,"->",end=' ')
                else:
                    print(temp.data,end=' ') #temp.data means first node's data
                temp=temp.next#establishing link
                
    def bubble_sort(self):
        T=self.head
        p=None
        c=0
        while T.next!=None:
            f=0
            t = self.head
            while t.next != p:
                if t.data > t.next.data:
                    f=1
                    t.data, t.next.data = t.next.data, t.data
                c=c+1
                t=t.next
            if(f==0):
                break
            p=t
            T=T.next
        print(c)
        
obj=SLL()
#node creation_initialising
n=Node(2)#so n.data in Node class will be 10
obj.head=n   #assigning first node as head
n1=Node(1)
n.next=n1 #next node value
n2=Node(4)
n1.next=n2
n3=Node(3)
n2.next=n3
n4=Node(5)
n3.next=n4
n5=Node(6)
n4.next=n5
n6=Node(7)
n5.next=n6 #next node value
n7=Node(8)
n6.next=n7
obj.display()
print()
obj.bubble_sort()
obj.display()


