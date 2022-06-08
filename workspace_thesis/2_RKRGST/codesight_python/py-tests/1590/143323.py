from sys import *
def f(n):
	ans = 0
	while(n):
		ans += n%10
		n = n // 10
	return ans
for x in stdin:
	N, A, B = map(int,x.split())
	ans = 0
	for i in range(N):
		s = f(i+1)
		if( s>=A and s<=B ):
			ans += i+1
	stdout.write(str(ans)+'\n')