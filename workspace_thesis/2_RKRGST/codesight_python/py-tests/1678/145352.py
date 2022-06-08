from sys import * 
letras='abcdefghijklmnopqrstuvwxyz'
while(1):	
	n = int(stdin.readline())
	M = []
	for i in range(n):
		v = [0]*26
		s = stdin.readline()
		for c in s:
			if(c in letras):
				v[letras.index(c)] += 1
		M.append(v)
	ans = 0	
	for i in range(n-1):		
		for j in range(i+1,n):
			c = 0			
			for k in range(26):
				if(M[i][k]+M[j][k])%2==1:
					c += 1
			if(c<2):
				ans += 1				
	stdout.write(str(ans)+'\n')
