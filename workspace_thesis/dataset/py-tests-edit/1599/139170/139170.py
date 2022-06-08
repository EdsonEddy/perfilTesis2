def gcd(a,b):
   if b==0:return a
   return gcd(b,a%b)
t = int(input())
for i in range(t):
   a, b, c, d = map( int,input().split() )
   e = a*d + b*c
   f = b*d
   g = gcd(e,f)
   print("{}/{}".format(e//g,f//g))