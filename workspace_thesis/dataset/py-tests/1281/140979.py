import math
def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.extend([n])
    g=list(list(divs))
    return g
while True:
	pop=int(input())
	jk=[]
	n=divisors(pop)
	for i in n:
		y=int(i)
		jk.append(y)
	gh=sorted(jk)
	gh=set(gh)
	gh=sorted(list(gh))
	pop=str(pop)
	yuu='Divisores de '+pop+':'
	if pop=='1':
		print('Divisores de 1: 1')
	else:
		print(yuu,*gh)