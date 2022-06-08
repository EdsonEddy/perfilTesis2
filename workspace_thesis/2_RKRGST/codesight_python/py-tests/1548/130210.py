import sys
if __name__=='__main__':
    for x in sys.stdin:      
      t = int(x)
      while t:
         t -= 1
         n = int(input())
         mx = mn = -1
         if n%2==0:
            mx = mn = 2
            while n%2==0:
               n = n // 2
         i = 3
         while i*i <= n:
            if n%i == 0:
               if mn==-1: mn = i
               if mx < i: mx = i
               while n%i == 0:
                  n = n // i
            i += 2
         if n != 1:
            if mn == -1: mn = n
            if mx < n :  mx = n
         if mn == mx:
            print('Equilibrio')
         else: print('[{},{}]'.format(mn,mx))

