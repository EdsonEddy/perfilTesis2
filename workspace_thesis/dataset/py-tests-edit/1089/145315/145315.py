from math import log10
n=int(input())
cd=int(log10(n))
if cd%2==0:
 cd=cd//2
 n=n//(10**cd)
 ep=n%10
 print(ep)
else:
 print('*')