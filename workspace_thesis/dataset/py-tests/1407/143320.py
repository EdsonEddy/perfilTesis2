from sys import * 
t = int(stdin.readline())
for j in range(t):
	n = int(stdin.readline())
	v = []
	while(len(v)<n):
		v += [int(x) for x in stdin.readline().split()]
	ans = 0
	for i in range(1,n-1):
		if(v[i]>v[i-1] and v[i]>v[i+1]):
			ans += 1
	stdout.write(str(ans)+'\n')