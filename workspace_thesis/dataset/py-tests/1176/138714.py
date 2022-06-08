#Banco vitalicio
import sys

if __name__ == '__main__':
	for line in sys.stdin:
		N, M, P = list(map(int, line.rstrip().split()))
		personas = []
		for i in range(N):
			x, y = input().split()
			x = int(x)
			personas.append((y, x))
		z = 0
		tiempos = []
		primero = personas[0]
		aux = []
		for i in personas:
			if i[1] == primero[1]:
				aux.append(i)
			else:
				z += 1
				tiempos.append(aux)
				aux = []
				aux.append(i)
				primero = i
		tiempos.append(aux)
		personas = []
		for i in tiempos:
			i.sort(reverse = True)
			personas += i
		s = 'Mil disculpas, regrese mañana'
		t = personas[0][1]
		M -= t
		for i in personas:
			if M >= P :
				t += P
				print(t)
				M -= P
			else:
				print(s)



