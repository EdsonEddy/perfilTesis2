import sys
if __name__=='__main__':
    for x in sys.stdin:
    	t = int(x)
    	while t:
    		t -= 1
    		n = int(input())
    		ocho = "8"
    		if n==0:print(1)
    		elif n==1:print(0)
    		else:
    			if(n%2==1):print(4,end='')
    			print(ocho*(n//2))
    