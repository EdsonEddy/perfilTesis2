from sys import *
n = int(stdin.readline())
v = []
while(len(v)<n):
	v += [int (x) for x in stdin.readline().split()]
sw = 1
for i in range(n//2):
	if(v[i]!=v[n-i-1]):
		sw = 0
		break
if(sw):stdout.write('SI\n')
else : stdout.write('NO\n')