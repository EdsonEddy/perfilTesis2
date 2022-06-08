

def find(data, i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]


def union(data, i, j):
    pi, pj = find(data, i), find(data, j)
    if pi != pj:
        data[pi] = pj


def connected(data, i, j):
    return find(data, i) == find(data, j)


casos = int(input())
i = 0
while i < casos:
	try:
		N, M = list(map(int, input().rstrip().split()))
	except ValueError:
		continue

	data = [i for i in range(N+10)]
	for j in range(M):
		x, y = list(map(int, input().rstrip().split()))
		union(data, x, y)
	x, y = list(map(int, input().rstrip().split()))
	if connected(data, x, y):
		print('SI')
	else:
		print('NO')
	i+=1
