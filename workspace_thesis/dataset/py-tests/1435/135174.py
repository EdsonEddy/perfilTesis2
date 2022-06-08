import math
n, k = map(int, input().split())
cd=int(math.log10(n))+1
n=n//10**(cd-k)
k=n%10
print(cd,k)