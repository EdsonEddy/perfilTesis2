def fib(n): 
	a, b = 0, 1 
	for _ in range(n): 
		a, b = b, a+b 
	return a 
for i in range(int(input())):
	n = int(input())
	if n<=200:
		item = fib(n)
	print(item)	
	