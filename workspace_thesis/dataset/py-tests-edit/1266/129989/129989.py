from sys import *
while 1>0:
 n,x=map (int,input ().split ())
 c=1
 e=0.0
 t=input ().split ()
 for i in t:
  te=int (i)
  e=e+(te*x**(n-c))
  c=c+1
 print (e)