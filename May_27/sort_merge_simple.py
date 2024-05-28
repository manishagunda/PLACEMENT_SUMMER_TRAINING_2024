a=[2,5,7,9]
b=[1,3,6,7,10,13]
c=[]
i,j=0,0
while i<len(a) and j<len(b):
    if(a[i]<b[j]):
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j])
        j=j+1
if (j<len(b)):
    c.append(b[j]) #c.extend(a[i:])
    j=j+1
if (i<len(a)):
    c.append(b[i])
    i=i+1
print(c)