n=int(input());
contador=1;
control=10;
while control<=n:
    contador=contador+1;
    control=control*10;
if contador%2==1 and contador==5:
	p=n//10
	q=p//10
	r=q//10
	m=q%10
	print(m)
if contador%2==1 and contador==3:
	q=n//10
	r=q//10
	m=q%10
	print(m)
if contador%2==1 and contador==1:
	print(n)

elif contador%2==0:
	print("*")