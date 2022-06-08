def bina(n):
    b=''
    while n//2!=0:
        b=str(n%2)+b
        n=n//2
    return str(n)+b
while True:
	n=int(input())
	h=bina(n)
	c=len(h)
	print(c)