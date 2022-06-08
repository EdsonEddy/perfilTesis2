from math import log10
n, k = map(int,input().split())
a=n
ni=0
nn=int(log10(n)+1)
while n>0:
    dig1=n%10
    n=n//10
    ni=ni*10+dig1
for i in range(k):
    dig=ni%10
    ni=ni//10
print(nn,dig)