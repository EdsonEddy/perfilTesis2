n,m,a,b=map (int,input ().split ())
c=1
while c <=(n-2):
 f=a+b
 a=b
 b=f
 cf=f%m
 c=c+1
print (cf)