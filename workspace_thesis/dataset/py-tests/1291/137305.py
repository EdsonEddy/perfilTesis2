va=1
while va!=0:
 val=input ().split ()
 if len (val)!=0:
  s=0
  for i in val:
   d=int (i)
   s=s+d
  print (s)
 else:
  va=0