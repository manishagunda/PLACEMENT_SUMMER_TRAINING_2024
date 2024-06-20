n=12412
n=str(n)
l=len(n)
if l%2!=0:
    k=l//2
    m=(n[k+2:])
    m=m[::-1]
    g=n[:k+2]
    if ((g+m)==n):
        print(g+m)
        int(n[k])=int(n[k])+1
        h=n[:k:-1]
        print(n)
        
        
    