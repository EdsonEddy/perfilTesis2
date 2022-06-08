t=int(input())
for i in range(t):
	n=int(input())
	ans=0
	sw=0
	while n>0:
		if n%100==96:
			sw=1
			break
		n//=10
	if sw==1:
		print("APLAZADO!")
	else:
		print("TE SALVAS :D")