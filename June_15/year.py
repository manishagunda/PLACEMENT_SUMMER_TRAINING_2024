'''
ip:
360days year
30 days month
6 days week
'''
n=65476
y=n//360
n=n-(y*360)
m=n//30
d=n-(m*30)
print(y,"years",m,"months",d,"days")