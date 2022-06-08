t=int(input())
p=[]
for i in range(t):
	x=input()
	p.append(x[::-1])
for i in range(len(p)-1,-1,-1):
	print(p[i])
	
