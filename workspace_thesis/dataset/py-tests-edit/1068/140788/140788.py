x=int(input())
if 1<=x<=100:
  while x > 0:
     x-=1
     n=int(input())
     c=0
     antes=0
     if 1 <= n <= 100:
         while n >0:
             n-=1
             palabra=str(input())
             if len(palabra)<=20:
                 if palabra!='porque':
                     c+=1
                 else:
                     antes=c
     print(antes)