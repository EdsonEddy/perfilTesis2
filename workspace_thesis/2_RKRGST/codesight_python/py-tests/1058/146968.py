x=int (input ())
for i in range (x):
 n=int (input ())
 cn=input ().split ()
 lista=[]
 c=0
 for j in cn:
  a=int (j)
  lista.insert (c,a)
  c=c+1
 lista.sort ()
 cadena=''
 for k in lista:
  dat=str (k)
  if n==1:
   cadena=cadena+dat
  else:
   cadena=cadena+dat+' '
  n=n-1
 print (cadena)