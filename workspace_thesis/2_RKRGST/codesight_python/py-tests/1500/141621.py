n=int(input(""))
v=list(map(int,input().split()))
aux=[v[i] for i in range(len(v))]
aux.reverse()
if (v==aux):
	print("SI")
else:
	print("NO")