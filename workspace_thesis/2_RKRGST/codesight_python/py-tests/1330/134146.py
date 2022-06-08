S,R = map(str,input().split())
R = int(R)	
l = len(S)-R
c,a = 0,[]
for i in S:
	c=c+1
	if c>l:
		a.append(i)
for j in a:
	print(j, end='')
for i in range(0,l):
	print(S[i], end='')