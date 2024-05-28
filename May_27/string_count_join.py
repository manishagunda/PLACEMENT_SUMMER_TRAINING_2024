s="aaabbaaaaddd"
c=[] #c=''
count=1
current=s[0]
for i in range(1, len(s)):
        if s[i] == current:
            count=count+ 1
        else:
            c.append(current + str(count)) #c=c+s[i]+count
            current = s[i]
            count = 1
c.append(current+ str(count))
print(c)
print(''.join(c))
            
            
