'''ip: asd123!@#  op: 1
ip:  123456789    op: 3
ip: ab    op:6
ip: A1234B  op:2
ip: A!234b op:2
ip: A1234a@4 op:-1
'''

s=input()
n1=len(s)
c,m,n,o=-1,-1,-1,-1
c1,m1,n1,o1=-1,-1,-1,-1
if(n1>=8):
    for i in s:
        if i.isdigit():
            c=0
            break
    for i in s:
        if i.isalpha():
            m=0
            break
    for i in s:
        if not i.isalnum():
            n=0
            break
    for i in s:
        if i.isupper():
            o=0
            break
else:
    for i in s:
        if i.isdigit():
            c1=0
            break
    for i in s:
        if i.isalpha():
            m1=0
            break
    for i in s:
        if not i.isalnum():
            n1=0
            break
    for i in s:
        if i.isupper():
            o1=0
            break

if ((c==0) and (m==0) and (n==0) and (o==0)):
    print("valid")
else:
    print("invalid")
    if(n1<8):
        if((c1==-1) and (m1==-1) and (n1==-1) and (o1==-1)):
            print(8-n1)
        else:
            print(-(c1+m1+n1+o1))
    else:
        print(-(c+m+n+o))
                
