from math import log10
n=int(input())
c=1
cd=int(log10(n))
nn=0
a=n
while c<=cd:
 x=a%10
 nn=(nn*10)+x
 a=a//10
 c=c+1
nn=(nn*10)+a
if nn==n:
 print('S')
else:
 print('N')