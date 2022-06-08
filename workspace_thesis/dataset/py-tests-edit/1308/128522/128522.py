import sys
A = [[0 for j in range(21)] for i in range(21)]
for i in range(21):
	A[0][i] = i
	A[i][0] = 0
for i in range(1,21):
	for j in range(1,21):
		A[i][j] = A[i-1][j] + A[i][j-1]
if __name__=='__main__':

    for x in sys.stdin:
    	i, j = map(int,x.split())
    	print(str(A[i][j]))
        