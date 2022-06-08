n=int(input())
for i in range(n):
	k=int(input())
	d=input().split()
	t=[]
	for i in d:
		t.append(int(i))
	print(*sorted(t))