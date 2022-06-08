import sys
def dp(x, y, n, m):
    memo = [[0 for i in range(m+1)]for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1] == y[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
 
    return memo[n][m]
 
for i in sys.stdin:        
    x = i
    y = input()    
    print(dp(x,y,len(x),len(y)))        