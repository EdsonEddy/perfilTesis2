from math import *
t=int(input())
for i in range(t):
	n,k=map(int,input().split())
	tam=int(log10(n))+1
	k=k%tam
	while k>0:
		k-=1
		n=n//(10**(tam-1))+n*10
		n=n%(10**tam)
	print(n)
