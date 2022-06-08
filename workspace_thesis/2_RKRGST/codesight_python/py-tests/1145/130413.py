while 1:
	n=int(input())
	if 1<=n<200:
		for j in range(n):
			aa=int(input())
			a=1
			b=0
			if aa!=0:
				for i in range(aa):
					a,b=b,a+b
					if i==aa-1:
						print(b)