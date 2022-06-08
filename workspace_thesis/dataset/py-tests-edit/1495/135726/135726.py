import sys
f = [1,1]
for i in range(2,21):
   f.append(f[-1]+f[-2])
v =[1]*100
p = [2]
i = 3
while(i<100 and len(p)<21):
   if(v[i]):
      p.append(i)
      j=i*i
      while(j<100):
         v[j] = 0
         j += i
   i += 2
t = [1,3,6]
for j in range(3,21):
   t.append(t[-1]+t[-2]+t[-3])
for z in sys.stdin:
   n, x = map(int,z.split())
   ans = 0
   for i in range(n):
      if(i%2==0):
         ans += (t[i]*(x**p[i]))/f[i]
      else: ans -= (t[i]*(x**p[i]))/f[i]
   print("{:.2f}".format(ans))
