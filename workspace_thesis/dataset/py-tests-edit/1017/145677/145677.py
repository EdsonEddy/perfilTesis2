from sys import * 
def cambio(num,base):
	return int(str(num),base)
def maxi(num):
	c = 0
	while num:
		c = max(c,num%10)
		num = num // 10
	return c+1
t = int(input())
for j in range(t):
	n, m = map(int,input().split())
	mx = maxi(m)
	while( n!=cambio(m,mx) ):mx += 1
	print(mx)
