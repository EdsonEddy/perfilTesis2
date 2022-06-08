r=int(input())
for i in range(r):
	a, b, c= map(int, input().split(" "))
	bs=[0]
	bs.append(a)
	bs.append(b)
	bs.append(c)
	cs=sorted(bs)
	c=i+1
	print("Case "+str(c)+":",cs[2])



