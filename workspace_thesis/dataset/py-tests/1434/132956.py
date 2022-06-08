n = int(input())
copian = n
nnum = 0
while n > 0:
	nnum = nnum*10 + n%10
	n//=10
if nnum == copian:
	print("S")
else:
	print("N")