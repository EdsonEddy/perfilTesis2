def bina(n):
    binario=''
    while n//2!=0:
        binario=str(n%2)+binario
        n=n//2
    return str(n)+binario
while True:
	n=int(input())
	b=bina(n)
	c=len(b)
	print(c)