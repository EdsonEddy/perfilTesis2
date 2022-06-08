n, i, j = [int(x) for x in input().split()]
v = [int(x) for x in input().split()]
v[i:j+1] = sorted(v[i:j+1])
for x in v[0:len(v)-1]:
	print(x, end=' ')
print(v[len(v)-1])