'''
job scheduling
[(1,3) (2,5) (4,6) (6,7) (5,8) (7,9)]
[5,6,5,4,11,2]
op: 17'''

m=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
l1=[5,6,5,4,11,2]
l2=l1.copy()
for i in range(1,len(m)):
    for j in range(i):
        if m[j][1]<=m[i][0]:
            if(l2[j]+l1[i]>l2[i]):
                    l2[i]=l2[j]+l1[i]
                    
          
    
        
print(max(l2))
        

