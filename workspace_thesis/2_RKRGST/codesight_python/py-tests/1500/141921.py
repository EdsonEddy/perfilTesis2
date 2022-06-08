n=int(input())
v=input().split()
ans=1
tam=len(v)
for i in range(tam):
	if v[i]!=v[tam-i-1]:
		ans=0
		break
if ans:
	print("SI")
else:
	print("NO")