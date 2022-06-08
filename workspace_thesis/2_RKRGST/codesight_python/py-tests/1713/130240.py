from sys import stdin
for test in stdin:
	res=0
	test1=int(test)
	for i in range(test1):
		x=int(input())
		res+=x
	print(res)