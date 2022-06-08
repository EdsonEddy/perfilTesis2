t = int(input())
for i in range(t):
   n = int(input())
   m = n
   while(1):
      c = 0
      while(n):
         c += (n%10)**2
         n = n//10
      n = c
      if(n==m or n==1 or n==4):
         break
   if(n==1):
      print("Feliz")
   else: print("Triste")
