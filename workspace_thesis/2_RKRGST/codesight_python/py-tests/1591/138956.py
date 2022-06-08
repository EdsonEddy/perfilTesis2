n=int(input())
for i in range (n):
	a=int(input())
	r=0
	b=1
	while a>0:
	    d=a%10
	    a=a//10
	    if d==2 or d==3 or d==5 or d==7:
	        r=r+d*b
	        b=b*10    
	if r==0:
	   print("-1")
	else:
	   print(r)
