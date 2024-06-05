'''ip  [4,7,1,4,1,3] first home 4 units, second 7 units, third 1 unit...
3 rats
5 units per rat

op: 2'''
a=[6,5,7,3,2]
a.append([5,8])
print(a)
a.extend([4,2,1])
print(a)
a.append(7.8)
print(a)
print(len(a))
a.extend([2])
print(len(a))
a.extend("7.8")
a.extend("hi")
print(len(a))
print(a)
a={5,5.0,'5',3,2}
print(len(a))
print(a)
a={5,5.0,'5',(5,2),'5,2'}
print(a)
a={5,5.2,'5',(5,2),'''[5,2]''',(2,5)} #list not taken in set
print(a)
a={5,1,'5',(5,2),1,(2,5),"hi","hi",True,False}#1=True+duplicates
print(a)
a={5,1,'5',(5,2),1,(5,2,),"hi","hi",
