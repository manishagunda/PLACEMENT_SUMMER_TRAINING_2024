#input 13 then output 13
#input 14 then output 17 primenumber

a=int(input())
while(1):
    c=0
    for i in range(2,(a//2)+1):
        if (a%i==0):
            c=c+1
            break
    if(c==0):
        print(a)
        break
    else:
        a=a+1
   
