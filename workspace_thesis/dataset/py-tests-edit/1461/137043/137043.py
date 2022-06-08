def felices(n):
	c=0
	for i in n:
		c=c+(pow(int(i),2))
	return c
def feliz(a):
	if a==4:
		return False
	m=felices(list(str(a)))
	if m==1:
		return True
	else:
		return feliz(m)
b=int(input())
for j in range(b):
	x=int(input())
	if feliz(x)==True:
		print("Feliz")
	else:
		print("Triste")