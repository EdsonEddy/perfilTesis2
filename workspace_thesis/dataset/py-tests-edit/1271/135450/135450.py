n=int(input())
for i in range(1,n+1,1):
	n=int(input())
	
	if n<=1000:
		p=n//100
		q=n%100
		r=q//10
		s=q%10
		o=1
		if p>=1:
			for i in range(p,0,-1):
				o=o*i
				p=o
		o=1
		if r>=1:
			for i in range(r,0,-1):
				o=o*i
				r=o
		o=1
		if s>=1:
			for i in range(s,0,-1):
				o=o*i
				s=o
		t=s+r+p
		if t==n:
			print("Y")
			
		else:
			print("N")
			
	elif n>1000:
		print("Y")
