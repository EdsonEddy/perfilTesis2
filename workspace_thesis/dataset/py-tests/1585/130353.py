import sys
if __name__=='__main__':
   for x in sys.stdin:      
      n = int(x);
      a = b = 1
      v = [int (i) for i in input().split()];
      for i in range(3):         
         if v[i]<n: a += 1
      v = [int (i) for i in input().split()];
      for i in range(3):         
         if v[i]<n: b += 1
      print(a*b)