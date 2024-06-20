'''
ip : tu5g2k1h8
     g5g8gd6h3
op:
    865312 largest even num'''

a="tu5g2k1h8"
b="g5g8gd6h3"
c=set()
for i in a:
    if i.isdigit():
        c.add(i)
for i in b:
    if i.isdigit():
        c.add(i)
c=sorted(list(c))
for i in range(len(c)):
    if int(c[i])%2==0:
        c[i],c[-1]=c[-1],c[i]
        break
o=len(c)
m=sorted(c[:o-1])
m=m[::-1]
m.append(c[-1])
print(''.join(m))







