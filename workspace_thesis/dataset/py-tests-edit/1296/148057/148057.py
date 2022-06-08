n=int (input ())
vec=[]
c=0
for i in range (n):
 cad=input ()
 ta=len (cad)
 nc=''
 for j in range (ta):
  ta=ta-1
  l=cad [ta]
  nc=nc+l
 vec.insert (c,nc)
 c=c+1
c=n-1
for i in range (n):
 print (vec [c])
 c=c-1