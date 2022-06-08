def isPrime(n):
   if(n==1):return 0
   if(n==2):return 1
   i=3
   while(i*i<=n):
      if(n%i==0):return 0
      i += 2
   return n%2
a, b = map(int,input().split())
ans = 0
for i in range(a,b+1):
   ans += isPrime(i)
print(ans)