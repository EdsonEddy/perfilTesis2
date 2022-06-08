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
letras = 'abcdefghijklmnopqrstuvwxyz'
for i in sys.stdin:        
    x = ''
    for c in i:
    	if(c in letras or c in letras.upper()):
    		x += c
    i = input()
    y = '' 
    for c in i:
    	if(c in letras or c in letras.upper()):
    		y += c
    # print(len(x),len(y))  
    ans = dp(x,y,len(x),len(y))     
    print('Compatibilidad: {:.2f} %'.format(ans*100/min(len(x),len(y)))) 