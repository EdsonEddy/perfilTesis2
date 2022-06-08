n=int(input())
h=n//3600
m=n%3600
t=m%60
m=m//60
s=t
print(str(h)+" "+str(m)+" "+str(s))