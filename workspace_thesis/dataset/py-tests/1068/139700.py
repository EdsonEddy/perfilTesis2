t = int(input())
for i in range(t):
	n = int(input())
	sw = 1
	ans = 0
	for j in range(n):
		x = input()
		if(x=='porque'):
			sw = 0
		if(sw):ans += 1
	print(ans)
