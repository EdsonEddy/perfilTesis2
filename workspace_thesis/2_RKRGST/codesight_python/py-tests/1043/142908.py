
n=int (input ())
for i in range (n):
 pi,pa=map (int,input ().split ())
 p=0
 ms=pi+pa
 sw=1
 while sw==1:
  pi=pi-3
  pa=pa-2
  if pi>=0 and pa>=0:
   p=p+1
  else:
   sw=0
 ms=ms-((p*3)+(p*2))
 print (p,ms)