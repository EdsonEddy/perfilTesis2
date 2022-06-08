import sys
def palindromo(k):
	aux=0
	while k>0:
		aux=(10*aux)+(k%10)
		k=k//10
	return aux
for n in sys.stdin:
	n=int(n)
	t=0
	for i in range(n):
		x=int(input())
		a=palindromo(x)
		if a==x:
			t=t+1
	print(t)