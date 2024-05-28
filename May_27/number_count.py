'''input 3 5 4 3 6 7 1 2 4 3 3 7 6
output
3-4
5-1
4-2
6-2
7-2
1-1
2-1'''
a=[3,5,4,3,6,7,1,2,4,3,3,7,6]
b=[]
for i in a:
    b.append(i)
for i in b:
    print(i,"-",a.count(i))
