import sys
def gcd(a,b):
   if b==0: return a
   return gcd(b,a%b)
for x in sys.stdin:
   a, b = map( int,x.split() )
   if gcd(a,b)==1:print('PRIMOS AMIGOS')
   else: print('PRIMOS ENEMIGOS') 