n,m=input().split()
s=len(n)
n,m=int(n),int(m)
if m<=s:
	m=(n%(10**(s-m+1)))/10**(s-m)
print(s,int(m))