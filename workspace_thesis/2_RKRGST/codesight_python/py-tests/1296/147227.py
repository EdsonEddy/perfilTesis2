cdp = int(input())
lista_pal = []
for i in range(0,cdp):
	pal = input()
	lista_pal.append(pal[::-1])
for j in reversed(lista_pal):
	print(j)