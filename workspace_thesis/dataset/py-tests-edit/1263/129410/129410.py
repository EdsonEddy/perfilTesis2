while True:
   a=1
   b,c=map(int,input().split())
   n=1
   cn=0
   while (n==1):
       x=(a+b)//2
       cn= cn+1
       if (x<c):
           a = x + 1
       elif (x>c):
           b=x-1
       elif (x==c):
           print(cn)
           break