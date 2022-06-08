def LCS(X, Y, m, n):
    a = [[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(0,m+1):
        for j in range(0,n+1):
            if i == 0 or j == 0:
                a[i][j] = 0
            elif X[i-1] == Y[j-1]:
                a[i][j] = a[i-1][j-1] + 1
            else:
                a[i][j] = max(a[i-1][j], a[i][j-1])

    print(a[m][n])

while True:
    try:
        a = input()
        b = input()
        m = len(a)
        n = len(b)
        LCS(a,b,m,n)
    except:
        break