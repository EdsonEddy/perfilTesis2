from sys import *
def primo(n):
	if  n<2:
		return False
	i=2
	while i*i<=n:
		if n%i==0:
			return False
		i+=1
	return True

for line in stdin:
	l=int(line)
	if primo(l)==True:
		print("ES PRIMO")
	else:
		print("NO ES PRIMO")
