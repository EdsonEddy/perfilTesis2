x=int(input())
l=list(map(int,input().split()))
v=l[::-1]
if v==l:
	print("SI")
else:
	print("NO")