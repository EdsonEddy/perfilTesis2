import sys
if __name__=='__main__':
    for x in sys.stdin:      
      t = int(x)
      while t:
         t -= 1
         n = int(input())
         c = mx = 0
         mapa = {}
         while n:
            n -= 1
            s = input().lower()

            x = ''
            for i in range(len(s)):
               if s[i]>='a' and s[i]<='z':
                  x+=s[i]
               elif len(x):                  
                  if mapa.get(x):
                     mapa[x] = mapa[x]+1
                  else: mapa[x]=1
                  if mapa[x]==mx:c += 1
                  if mapa[x]>mx:
                     mx = mapa[x]
                     c = 0
                  x = ''
         if c:print('Esto pasa choco')
         else:print('Vaya a Rehacer')         
