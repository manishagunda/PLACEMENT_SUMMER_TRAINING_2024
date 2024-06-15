'''
ip: 7262 sec
op 2h:1m:2s

ip:500sec
op:0h:8m:20s
'''
n=int(input())
h=n//3600
n=n-(h*3600)
m=n//60
s=n-(m*60)
print(h,"h",":",m,"m",":",s,"s")