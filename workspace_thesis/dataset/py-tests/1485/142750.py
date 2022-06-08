while True:
   c=int(input())
   s=0
   for i in range(c):
       a=input()
       b=a[::-1]
       if a==b:
           s=s+1
   print(s)