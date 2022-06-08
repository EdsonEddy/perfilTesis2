def primo(numero):
    for i in range(2,numero):
        if (numero%i)==0:
            return False
    return True
cas=int(input())
while cas>0:
	n=str(input())
	s=""
	for i in range(len(n)):
		if primo(int(n[i]))==True and int(n[i])!=1 and int(n[i])!=0:
			s=s+n[i]
	if s!="":
		print(s)
	if s=="":
		print(-1)		
	cas-=1