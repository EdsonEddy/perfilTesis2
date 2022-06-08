n=int(input())
l=list(map(int,input().split()))
x=(max(set(l), key=l.count))
c=0
for i in range(n):
	if l[i]!=x:
		c+=1
print(c)