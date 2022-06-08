a=input ()
c=0
v=[]
for i in range (len (a)):
 v.insert (c,a [c:len (a)])
 c=c+1
v.sort ()
for i in v:
 print (i)