'''input
f46fLK9y56u#@&56hIjbn6KJhA
output
lv-2
uv-2
lc-
uc-
d-
s- '''
s1="f46fLK9y56u#@&56hIjbn6KJhA"
uv,uc,lv,lc,d,s=0,0,0,0,0,0
for i in s1:
    if(i.isupper()):
        if i in "AEIOU":
            uv=uv+1
        else:
            uc=uc+1
    elif(i.islower()):
        if i in "aeiou":
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isdigit()):
        d=d+1
    elif(not i.isalnum()):
        s=s+1
print(uv,uc,lv,lc,d,s)
        
        
