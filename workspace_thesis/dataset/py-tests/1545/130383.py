import sys
def gcd(a, b):
   if b==0:return a
   else: return gcd(b,a%b)
def mcm(a,b):
   return a*b//gcd(a,b)
if __name__=='__main__':
   for x in sys.stdin:
      t = int(x)
      for i in range(t):
         a,b,c,d,e,f,g = input().split(' ')
         a,b,c,d,e,f=int(a),int(b),int(c),int(d),int(e),int(f)
         nf = mcm(a,e)//e
         nc = mcm(b,f)//f
         print(mcm(nf,nc))