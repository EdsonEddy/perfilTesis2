n=int (input ())
p=0
d=0
c=0
if n==1:
 c=c+1
else:
 while d <=n:
  d=d +(2**p)
  p=p+1
  c=c+1
print (c)