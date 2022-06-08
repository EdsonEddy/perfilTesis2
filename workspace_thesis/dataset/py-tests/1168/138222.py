t = int(input())
for j in range(t):
    s = set()
    a, b = map(int,input().split())
    for i in range(a,b+1):
      n = i
      if(n%2==0):
         s.add(2)
         while(n%2==0):
            n = n//2
      j = 3
      while j*j<=n:
         if(n%j==0):
            s.add(j)
            while(n%j==0):
               n = n//j
         j += 2
      if(n>1):
         s.add(n)
    print(len(s))
