n=int (input ())
for i in range (n):
 cant=int (input ())
 elementos=input ().split ()
 lista=[]
 c=0
 for j in elementos:
  da=int (j)
  lista.insert (c,da)
  c=c+1
 lista.sort ()
 cadena=''
 for k in lista:
  dat=str (k)
  if cant==1:
   cadena=cadena+dat
  else:
   cadena=cadena+dat+' '
  cant=cant-1
 print (cadena)