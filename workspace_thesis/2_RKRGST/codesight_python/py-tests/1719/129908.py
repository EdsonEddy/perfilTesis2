import sys
if __name__=='__main__':
    for x in sys.stdin:      
      n = int(x)
      v = []   
      while n:  
         mx = 0
         c = 0
         while len(v)<n:
            v = v+[ int (i) for i in input().split()]
         ans = n
         for i in range(n):
            if v[i] > mx: mx = v[i]      
            c += v[i]
         while (mx*ans)-c <= c:
            mx += 1
         print(mx)
         if len(v)>n:            
            v = v[n:]   
            n = v[0]
            v = v[1:]      
         else:
            n = 0
             