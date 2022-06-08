s=0
while s == 0:
	n=str(input())
	if n =="":
		s=1
	if s==0:
		a=int(n)
		v=["unu","du","tri","kvar","Kvin","ses","Sep","OK","Nau","dek"]
		for i in range (a):
			if a <=10:
				x=v[i]
			if a >= 20:
				d=a%10
				b=int(a/10)
				if d != 0:
					x=v[b-1]+"dek"+" "+v[d-1]
				if d == 0:
					x=v[b-1]+"dek"
			if a>10 and a < 20:
				e=a%10
				x="dek"+" "+v[e-1]
		print(x)