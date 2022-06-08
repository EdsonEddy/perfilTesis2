def numeros_felices(n):
	res=0
	for d in n:
		res=res+pow(int(d),2)
	return res
def es_feliz(a):
	if a==4:
		return False
	u=numeros_felices(list(str(a)))
	if u==1:
		return True
	else:
		return es_feliz(u)
casos=int(input())
for i in range(casos):
	g=int(input())
	if es_feliz(g)==True:
		print("Feliz")
	else:
		print("Triste")
