n=input()
c1,m1,n1,o1=0,0,0,0
for i in n:
    if i.isdigit():
            c1=1
    if i.isalpha():
            m1=1
    if not i.isalnum():
            n1=1
    if i.isupper():
            o1=1
m=4-(c1+m1+n1+o1)
if(len(n)+m)<8:
    print(8-len(n))
else:
    if(m==0):
        print(-1)
    else:
        print(4-m)
    
    