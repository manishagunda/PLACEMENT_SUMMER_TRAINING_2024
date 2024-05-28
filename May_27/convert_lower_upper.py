'''input
placements
output
plAcEmEnts'''
s=input()
c=""
for i in s:
    if i in "aeiou":
        i=i.upper()
        c=c+i
    else:
        c=c+i
print(c)
    
    
        
        
