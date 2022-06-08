from sys import stdin
def primo(n):
    i=2
    while (i**2)<=n:
        if(n%i==0):
            return False
        i=i+1
    if(n==1):
        return False
    else:
        return True
for n in stdin:
	n=int(n)
	if(primo(n)):
		print("ES PRIMO")
	else:
		print("NO ES PRIMO")