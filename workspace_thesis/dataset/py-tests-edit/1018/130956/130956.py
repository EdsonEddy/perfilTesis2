n=int (input ())
c=1
while c <=n:
 a,b=map (int,input ().split ())
 if a>b:
  print (">")
 else:
  if a <b:
   print ("<")
  else:
   print ("=")
 c=c+1