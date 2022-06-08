import sys
if __name__=='__main__':
    for x in sys.stdin:      
      n, s = map(int,x.split())
      v = []
      while len(v)<n:
         v = v + [int (i) for i in input().split()]
      i = j = 0
      c = v[0]
      while c!=s:
         if c<s:
            j += 1
            if j>=n:break
            c += v[j]
         if c>s:
            c -= v[i];
            i += 1
            if i>=n:break
            if i>j:
               j = i
               c = v[j]
      if s==c:print('{} {}'.format(i+1,j+1))
      else: print('-1')

