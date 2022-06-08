import sys
v=[]
for i in range(1,401):
   j = 0
   while(j<i and len(v)<401):
      v.append((1<<i)+(1<<j))
      j += 1
for x in sys.stdin:
   n = int(x)
   for i in range(n):
      if(i==n-1):print(v[i])
      else:print(v[i],end=' ')
