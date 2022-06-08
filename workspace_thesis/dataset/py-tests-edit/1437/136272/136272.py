n=int(input())
sw=True
while n>0:
	if (n%10)!=4 and (n%10)!=7:
		sw=False
		break
	n//=10
if sw==True:
	print("S")
else:
	print("N")