def Fa(n):
	F = []
	for i in range(1,n+1):
		for j in range(1,n+1):
			F.append(i)
	return F
def rey(n):
	R = []
	for i in range(1,n+1):
		for j in range(1,n+1):
			R.append(j)
	return R

n = int(input())
num = Fa(n)
den = rey(n)
for i in range(0,n**2):
	print(num[i],'/',den[i],sep='')