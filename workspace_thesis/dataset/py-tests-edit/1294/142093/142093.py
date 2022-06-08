import sys
def s(x,y):
	suma=0
	for i in range(x,y+1):
		suma=suma+v[i]
	return suma
v=[ ]
for n in sys.stdin:
	n=int(n)
	for i in range(n):
		n,a,b=map(int,input().split())
		v=list (map(int,input().split()))
		print(s(a,b))