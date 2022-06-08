from sys import *
t = int(input())
while(t):
	t -= 1
	ans = 1
	a ,b ,c = map(int,input().split())
	for x in range(-10,25):
		if(ans==0):break
		if(x*x<=c):
			for y in range(-10,101):
				if(ans==0):break
				if(y!=x and x*x + y*y <= c):
					for z in range(-10,101):
						if(ans==0):break
						if(z!=x and z!=y and x+y+z==a and x*y*z==b and x*x+y*y+z*z==c):
							print(x,y,z)
							ans = 0
	if(ans):
		print('Sin solucion')							
