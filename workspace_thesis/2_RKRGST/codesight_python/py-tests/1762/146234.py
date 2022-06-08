while True:
	num = int(input())
	arr = list(map(int,input().split()))
	nl,s = [],0
	for i in arr:
		if i not in nl:
			nl.append(i)
	for j in nl:
		if arr.count(j)%2==0:
			s = s+arr.count(j)//2
		elif arr.count(j)>2 and arr.count(j)%2!=0:
			s = s+(arr.count(j)-1)//2
	print(s)