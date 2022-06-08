def isPrime(n):
	if(n%2==0):return 1
	i = 3
	while(i*i<=n):
		if(n%i==0):
			return 1
		i += 2
	return 0
t = int(input())
for i in range(t):
	n = int(input())
	a = b = n
	a+=1
	b-=1
	while(isPrime(a)):a += 1
	while(isPrime(b)):b -= 1
	print(a+b)
