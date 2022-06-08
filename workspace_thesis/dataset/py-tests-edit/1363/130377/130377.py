import sys
if __name__=='__main__':
   for x in sys.stdin:      
      n = len(x)
      ans = -1
      for i in range(n):
         if x[i]=='<':
            ans = max(ans,1)
            j = i + 1
            while (j<n) and (x[j]=='-'):
               j += 1
               ans = max(ans,j-i)               
            j = i + 1
            while (j<n) and (x[j]=='='):
               j += 1
               ans = max(ans,j-i)
         elif x[i]=='>':
            ans = max(ans,1)
            j = i - 1
            while j>=0 and x[j]=='-':
               ans = max(ans,i-j+1)
               j -= 1
            j = i - 1
            while j>=0 and x[j]=='=':
               ans = max(ans,i-j+1)
               j -= 1
      print(ans)