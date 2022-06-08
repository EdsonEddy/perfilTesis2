while 1>0:
 n=int (input ())
 lh=input ().split ()
 lv=input ().split ()
 p=1
 ch=1
 for i in lh:
  l=int (i)
  if l <n and l!=0:
   p=p+1
   ch=ch+1
 for j in lv:
  l=int (j)
  if l <n and l!=0:
   p=p+ch
 print (p)