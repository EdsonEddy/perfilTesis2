n=input()
l=len(n)
n=int(n)
if l%2 !=0 :
	l=l//2
	d=10**l
	n=n//d
	print(n%10)
else:
	print('*')
	