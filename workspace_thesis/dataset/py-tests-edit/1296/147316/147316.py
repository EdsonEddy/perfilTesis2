n=int(input())
p=[]
for i in range(n):
	n=input()
	p.append(n)
e=p[::-1]
for j in e:
	print(j[::-1])