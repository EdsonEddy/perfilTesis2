import sys
Max = int(1e3 + 1)
prime = [1]*Max
v = [0,0,1]
i = 3
c = 1
while i*i<Max:
   if prime[i]:
      c += 1
      j = i*i
      while j<Max:
         prime[j] = 0
         j += i
   v.append(c)
   v.append(c)
   i += 2
while i<Max:
   if prime[i] and i%2==1:
      c += 1
   v.append(c)
   i += 1
a, b = map(int,input().split())
print(v[b]-v[a-1])