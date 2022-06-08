import sys

def sumas(x,y):
	suma=0
	for k in range(x,y+1):
		suma+=v[k]
	return suma


for n in sys.stdin:
	n=int(n)
	for i in range(n):
		m,a,b=map(int,input().split())
		v=list(map(int,input().split()))
		print(sumas(a,b))
