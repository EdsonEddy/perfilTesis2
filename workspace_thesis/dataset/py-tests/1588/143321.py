from sys import * 
t = int(stdin.readline())
for j in range(t):
	n = int(stdin.readline())
	v = []
	while(len(v)<n):
		v += [int(x) for x in stdin.readline().split()]
	ans = 0
	for i in v:
		if( i%3 == 0 ):
			ans += i
	stdout.write('La suma es '+str(ans*2)+'\n')