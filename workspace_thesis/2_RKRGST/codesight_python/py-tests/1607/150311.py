import sys
for cp in sys.stdin:
    n=int(cp)
    m=[[0 for i in range(n)]for j in range(n)]
    k=1
    for i in range(n):
       for j in range(i,n-i):
         m[i][j]=k
         m[j][i]=k
         m[n-i-1][n-j-1]=k
         m[n-j-1][n-i-1]=k
       if k<=n/2:
          k+=1
       else:
          k-=1
    for i in range(n):
       for j in range(n):
           print(m[i][j],end=" ")
       print()
