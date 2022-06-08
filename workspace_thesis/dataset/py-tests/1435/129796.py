from math import log10
n,k=map (int,input ().split ())
cd=int (log10 (n)+1)
c=1
cd2=cd
while c <=k:
 d=n//(10**(cd2-1))
 n=n%(10**(cd2-1))
 c=c+1
 cd2=cd2-1
print (cd,d)