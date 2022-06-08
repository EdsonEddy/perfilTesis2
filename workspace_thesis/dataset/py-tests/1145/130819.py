x=int (input ())
for i in range (0,x):
 año=int (input ())
 c=1
 a=1
 b=0
 while c <=año:
  f=a+b
  a=b
  b=f
  c=c+1
 print (f)