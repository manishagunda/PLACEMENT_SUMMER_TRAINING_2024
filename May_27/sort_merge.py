'''input
2 5 7 9
1 3 6 7 10 13
output
1 2 3 5 6 7 7 9 10 13'''

#static
l1=[2,5,7,9]
l2=[1,3,6,7,10,13]
l=l1+l2
l.sort()
print(l)

#dynamic
list1=[]  
list2=[]  
num1=int(input("Enter number of elements for first list:"))  
for i in range(1,num1+1):  
    b=int(input("Enter element:"))  
    list1.append(b)  
  
num2=int(input("Enter number of elements for second list:"))  
for i in range(1,num2+1):  
    d=int(input("Enter element:"))  
    list2.append(d)  
  
list3=list1+list2  
list3.sort()  
print("Sorted list is:",list3)  



