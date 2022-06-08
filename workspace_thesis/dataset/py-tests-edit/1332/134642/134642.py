x=input ()
voc="aAeEiIoOuUyY"
nc=""
for i in x:
 l=i
 if l not in voc:
  nc=nc+"."+l.lower ()
print (nc)