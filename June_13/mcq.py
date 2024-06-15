l=[5,"hi",6.7,4,"hi"]
print(id(l[0]))
print(id(l[1]))
print(id(l[4])) #1,4 same id 
l=[5,"hi",6.7,4,"hi"]
l[4]=l[4]+'i'
print(id(l[0]))
print(id(l[1]))
print(id(l[4])) #list l[0] is address bcz address are kept in order

