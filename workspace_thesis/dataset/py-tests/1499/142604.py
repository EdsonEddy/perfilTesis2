n=int(input())
x=input()
v=list(map(int,x.split()))
pos=0
b=0
for i in range(1,len(v)):
	if v[i-1]<v[i]:
		pos=i
	else:
		break
for i in range(pos+1,len(v)):
	if v[i-1]==v[i]:
		pos=i
	else:
		break
for i in range(pos+1,len(v)):
	if v[i-1]>v[i]:
		pos=i
	else:
		break
if pos+1==n:
	print("SI")
else:
	print("NO")