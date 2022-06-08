while True:
	n,m=input().split()
	n,m=int(n),int(m)
	if(n>0 and m>0):
		if m%2!=0 or m==n or n>m:
			print(-1)
		else:
			a=(4*n-m)/2
			b=(m-2*n)/2
			if b<0 or a<0:
				print(-1)
			else:
				print(int(a),int(b))
	else:
		break