while True:
   e,v=map(int,input().split())
   x=input().split()
   s=0
   for o in range(e):
       for i in x:
           e=e-1
           f=e
           y=(int(i))
           p=v**f
           r=y*p
           s=s+r
       print(float(s))
       break