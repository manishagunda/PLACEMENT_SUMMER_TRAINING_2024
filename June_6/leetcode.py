#leetcode 1221
s="RLRL"
c=0
r=0
for i in s:
    if i=='R':
        c=c+1
    elif i=='L':
        c=c-1
    if c==0:
        r=r+1
print(r)
#2325
key = "the quick brown fox jumps over the lazy dog"
b=''
c=''
msg="vkbs bs t suepuv"
for i in key:
    if(i not in b and i!=' '):
        b=b+i
for i in msg:
    if(i!=' '):
        c=c+chr(b.index(i)+97)
    else:
        c=c+' '
print(c)
#3120
w="aABbC"
a=set(w)
c=0
for i in a:
    if(i.islower() and i.upper() in a):
        c=c+1
print(c)
#520
a=input()
print(a.isupper() or a.islower or a.istitle())
#3121

   