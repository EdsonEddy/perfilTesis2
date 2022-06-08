import sys
def f(A,n):
	tur = 0
	i = 4
	while(n>0 and i>=0):
		if(A[i]<=n):
			tur += n//A[i]
			n %= A[i]
		i -= 1
	return (n,tur)
A=("Hielo","Roca","Hada")
B=("Fuego","Roca","Tierra")
C=("Dragon")
D=("Dragon")
E=("Agua")
F=("Acero","Hielo","Planta")
G=("Planta","Tierra")
H=("Agua","Roca","Tierra")
I=("Fuego","Hielo")
J=("Fuego","Roca","Acero")
def dup(v):
	for i in range(5):
		v[i] *= 2
	return v
def tipo(x,y,v):
	if(x=='Acero'):
		if y in A:
			v=dup(v)
	if(x=='Agua'):
		if y in B:
			v=dup(v)
	if(x=='Dragon'):
		if y in C:
			v=dup(v)
	if(x=='Hada'):
		if y in D:
			v=dup(v)
	if(x=='Electrico'):
		if y in E:
			v=dup(v)
	if(x=='Fuego'):
		if y in F:
			v=dup(v)
	if(x=='Hielo'):
		if y in G:
			v=dup(v)
	if(x=='Planta'):
		if y in H:
			v=dup(v)
	if(x=='Roca'):
		if y in I:
			v=dup(v)
	if(x=='Tierra'):
		if y in J:
			v=dup(v)
	return v
def index(v,n):
	m = n

def cad(s):
	ans =''
	for i in s:
		if(i!='\n' or i==' '):
			ans += i
	return ans
while(1):
	x = sys.stdin.readline()
	if(x!='\n'):
		# print('este es',x)		
		s1,a = x.split("\n")
		t1,a = sys.stdin.readline().split("\n")
		n1,a = sys.stdin.readline().split("\n")
		# print('este es n1',n1)
		n1 = int(n1)
		p1 = list(map(int,input().split()))
		s2 = cad(input())
		t2 = cad(input())
		n2 = int(cad(input()))
		p2 = [int(i) for i in input().split()]

		p1 = tipo(t1,t2,p1)
		p2 = tipo(t2,t1,p2)		
		p1.sort()
		p2.sort()
		ans1 = f(p1,n2)
		ans2 = f(p2,n1)
		if(ans1[0]==0 and ans2[0]==0 and ans1[1]==ans2[1]):
			print('Ganador:',s1 ,'Turnos',ans1[1])
			print('Ganador:',s2 ,'Turnos',ans1[1])
		elif(ans1[1]<ans2[1] and ans1[0]==0):
			print('Ganador:',s1 ,'Turnos',ans1[1])
		elif(ans2[0]==0):
			print('Ganador:',s2 ,'Turnos',ans2[1])
		else:
			print('No existe ganador')