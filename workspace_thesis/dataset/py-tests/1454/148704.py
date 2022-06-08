N,y=map(int,input().split())
def rotateMatrix(mat):
    for x in range(0, int(N / 2)):
        for y in range(x, N - x - 1):
            temp = mat[x][y]
            mat[x][y] = mat[y][N - 1 - x]
            mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]
            mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]
            mat[N - 1 - y][x] = temp
def displayMatrix(mat):
    for i in mat:
        print(*i)
mat=[]
for i in range(N):
    fil=list(tuple(map(int,input().split())))
    mat.append(fil)
f=(y//90)*3
for k in range(f):
    rotateMatrix(mat)
displayMatrix(mat)

