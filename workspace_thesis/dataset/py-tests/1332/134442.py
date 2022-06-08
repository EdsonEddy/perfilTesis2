x=input ()
vocales="aAeEiIoOuUyY"
n=""
for i in x:
 l=i
 if l not in vocales:
  n=n+"."+l.lower ()
print (n)
