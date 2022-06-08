t = int(input())
for i in range(t):
	n, m = list(map(int, input().rstrip().split()))
	pos = [x for x in range(n)]
	elem = list(map(int, input().rstrip().split()))
	sw = True
	i = 1
	while sw:
		maxi = max(elem)
		e = elem.pop(0)
		p = pos.pop(0)
		if e != maxi:
			elem.append(e)
			pos.append(p)
			continue
		if p == m:
			break
		else:
			i += 1
	print(i)

