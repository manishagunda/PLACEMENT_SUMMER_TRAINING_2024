#left and right sum difference 2574
nums=[10,4,8,3]
s=sum(nums)
x=0
r=[]
for i in nums:
    r.append(abs((x)-(s-i-x)))
    x=x+i
print(r)
#decoded xored array1720
encoded=[1,2,3]
first=1
res = [first]
for num in encoded:
    res.append(res[-1] ^ num)
print(res)
#leetcode 1859
'''is2 sentence4 This1 a3
op This is a sentence'''
s=input().split()
c=[0]*len(s)
for i in s:
    c[int(i[-1])-1]=i[:-1]
print(' '.join(c))



        


