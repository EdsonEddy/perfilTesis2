import sys
f = [1,1]
for i in range(2,41):
   f.append(f[-1]+f[-2])
v =[1]*1000
p = [2]
i = 3
while(i<1000 and len(p)<41):
   if(v[i]):
      p.append(i)
      j=i*i
      while(j<1000):
         v[j] = 0
         j += i
   i += 2
for z in sys.stdin:
   n, x = map(int,z.split())
   ans = 0
   for i in range(n):
      ans += f[i]/(p[i]*x)
   print("{:.2f}".format(ans))
