n=int(input())
m=str(input())
a="ABC"*n
e="BABC"*n
g="CCAABB"*n
ca=0
ce=0
cg=0
sw=0
for i in range (n):
	if m[i]==a[i]:
		ca=ca+1
	if m[i]==e[i]:
		ce=ce+1
	if m[i]==g[i]:
		cg=cg+1
v=[ca,ce,cg]
may=0
for j in range (3):
    if may < v[j]:
        may=v[j]
print(may)
if ca>0 and may==ca:
    print("Alvaro")
if ce>0 and may ==ce:
    print("Edwin")
if cg>0 and may ==cg:
    print("Gabriel")
