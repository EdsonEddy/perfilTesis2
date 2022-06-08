casos=int(input())
for i in range(casos):
	numero=int(input())
	h=input()
	m=h.split()
	for j in range(numero):
		m[j]=int(m[j])
	w=sorted(m)
	print(*w)