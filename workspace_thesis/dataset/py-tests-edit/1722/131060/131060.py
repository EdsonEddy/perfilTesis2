x=int(input())
cd=0
cu=0
for i in range (x):
	n=int(input())
	if n%2==0:
		cd=cd+1
	else:
		cu=cu+1
if cd>cu:
	print("Gana el jugador 2!")
if cu>cd:
	print("Gana el jugador 1!")
if cu==cd:
	print("Empate!")