n = int(input())
m = [0]*n
for i in range(n//2 + 1):
    m[i] = [0]*n
for i in range(n//2+1):
    for j in range(n):
        if j <= i or j + 1 >= n-i :
            m[i][j] = 1
m[n//2 + 1] = [1]*n
for i in range(n//2):
    for j in range(n):
        if j != n-1:
            print(m[i][j], end='')
        else:
            print(m[i][j])
for j in range(n):
    if j != n-1:
        print(m[n//2 + 1][j], end='')
    else:
        print(m[n//2 + 1][j])
for i in range(n//2-1, -1, -1):
    for j in range(n):
        if j != n-1:
            print(m[i][j], end='')
        else:
            print(m[i][j])
