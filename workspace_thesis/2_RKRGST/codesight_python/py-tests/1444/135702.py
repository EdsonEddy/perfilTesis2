t = int(input())
for i in range(t):
   n = int(input())
   c = 0
   while(n):
      d = n%2
      n = n//2      
      if(d==1):
         if(n%2==1):
            c += 1
         n = n//2     
   print(c) 
