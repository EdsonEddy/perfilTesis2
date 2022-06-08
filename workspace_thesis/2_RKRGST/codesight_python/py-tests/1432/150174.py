x, k, m = list(map(int, input().split()))
ac = 0
for i in range(k, k*x+1, k):
	ac = (ac + i%m)%m
print(ac)