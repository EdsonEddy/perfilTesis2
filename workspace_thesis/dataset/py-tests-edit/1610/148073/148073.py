cad=input ()
nc=''
c=0
for i in cad:
 if i=='1':
  c=c+1
 else:
  nc=nc+str (c)
  c=0
print (nc+str (c))