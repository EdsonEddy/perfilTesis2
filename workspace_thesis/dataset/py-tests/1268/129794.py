def ecu_v(c,p):
 v=(p-(2*c))/2
 return v
def ecu_g (p,v):
 g=(p-(4*v))/2
 return g
sw=0
while sw==0:
 c,p=map (int,input ().split ())
 if c!=0 and p!=0:
  x=ecu_v (c,p)
  y=ecu_g (p,x)
  if x==int (x) and y==int (y):
   if x>=0 and y>=0:
    print (int (y),int (x))
   else:
    print ('-1')
  else:
   print ('-1')
 else:
  sw=1