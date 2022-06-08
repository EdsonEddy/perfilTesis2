import sys
if __name__=='__main__':
    for x in sys.stdin:
   		a, b = map(int, x.split())
   		if a==0 or b==0:break
   		if b%2!=0:print(-1)
   		else:
   			vacas = (b//2) - a
   			gall = a-vacas
   			if gall>=0 and vacas>=0:
   				print(gall,vacas)
   			else:
   				print(-1)