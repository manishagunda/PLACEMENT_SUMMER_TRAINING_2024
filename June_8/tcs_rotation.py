#tcs
'''ip
school
3
L 2--->hoolsc
R 3--->oolsch
L 1--->chools
op
yes
hoc
sch,cho,hoo,ool'''
s="school"
k=3
l=""
a=input()
n=int(input())
str=''
for i in range(n):
    b=input()
    if b[0]=='L':
        str=str+a[int(b[2])]
    else:
        str=str+a[-int(b[2])]
str=list(str)
str.sort()
print(str)
b=[]
for i in range(len(a)-n+1):
    t=list(a[i:n+i])
    t.sort()
    b.append(t)
print(b)
for i in b:
    if i==str:
        print("yes")
        break
else:
    print("no")




    


