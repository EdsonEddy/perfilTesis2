from sys import *
for n in stdin:
	n=int(n)
	if n==0:
		break
	v=stdin.readline().split()
	ans=0
	for i in range(len(v)):
		ans+=int(v[i])
	stdout.write(str(ans)+'\n')
