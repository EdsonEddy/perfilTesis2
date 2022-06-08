v=1
while v!=0:
 x=input ().split ()
 if len (x)!=0:
  s=0
  for i in x:
   d=int (i)
   s=s+d
  print (s)
 else:
  v=0