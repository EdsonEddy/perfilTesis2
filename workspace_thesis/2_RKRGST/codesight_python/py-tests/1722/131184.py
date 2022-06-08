n=int(input())
c2=0
c1=0
for i in range (0, n):
	x=int (input())
	if x==1:
		c1=c1+1
	if x==2:
		c2=c2+1
if c1>c2:
	print("Gana el jugador 1!")
else:
	print("Gana el jugador 2!")