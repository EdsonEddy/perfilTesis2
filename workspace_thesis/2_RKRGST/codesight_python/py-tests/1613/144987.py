import sys
n = int(input())
s = set()
for i in range(n):
	a, b = map(int,input().split())
	t = (a,b)
	s.add(t)
print(len(s))